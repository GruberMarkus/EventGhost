# This file is part of EventGhost.
# Copyright (C) 2005 Lars-Peter Voss <bitmonster@eventghost.org>
# 
# EventGhost is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# EventGhost is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with EventGhost; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#
# $LastChangedDate$
# $LastChangedRevision$
# $LastChangedBy$

import threading
import os
from os.path import join
from eg.WinApi.Utils import GetMonitorDimensions
from eg.WinApi.Dynamic import BringWindowToTop, CreateEvent, SetEvent 
    
SKIN_DIR = join(os.path.abspath(os.path.split(__file__)[0]), "OsdSkins")
DEFAULT_FONT_INFO = wx.Font(
    18, 
    wx.SWISS, 
    wx.NORMAL, 
    wx.BOLD
).GetNativeFontInfoDesc()


def AlignLeft(width, offset):
    return offset


def AlignCenter(width, offset):
    return (width / 2) + offset


def AlignRight(width, offset):
    return width - offset

         
ALIGNMENT_FUNCS = (
    (AlignLeft, AlignLeft), # Top Left
    (AlignRight, AlignLeft), # Top Right
    (AlignLeft, AlignRight), # Bottom Left
    (AlignRight, AlignRight), # Bottom Right
    (AlignCenter, AlignCenter), # Screen Center
    (AlignCenter, AlignRight), # Bottom Center
    (AlignCenter, AlignLeft), # Top Center
    (AlignLeft, AlignCenter), # Left Center
    (AlignRight, AlignCenter), # Right Center
)


def DrawTextLines(dc, textLines, textHeights, xOffset=0, yOffset=0):
    for i, textLine in enumerate(textLines):
        dc.DrawText(textLine, xOffset, yOffset)
        yOffset += textHeights[i]
        
        

class OSDFrame(wx.Frame):
    """ A shaped frame to display the OSD. """
    
    @eg.LogIt
    def __init__(self, parent):
        wx.Frame.__init__(
            self, 
            parent, 
            -1,
            "OSD Window", 
            size=(0, 0),
            style=wx.FRAME_SHAPED
                |wx.NO_BORDER
                |wx.FRAME_NO_TASKBAR
                |wx.STAY_ON_TOP
        )
        self.bitmap = wx.EmptyBitmap(0,0)
        self.timer = threading.Timer(
            0.0,
            self.SetPosition, 
            ((-10000, -10000),)
        )
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.SetPosition((-10000, -10000))
        
        
    @eg.LogIt
    def ShowOSD(
        self, 
        osdText="", 
        fontInfo=None,
        textColour=(255, 255, 255), 
        outlineColour=(0, 0, 0),
        alignment=0, 
        offset=(0, 0), 
        displayNumber=0, 
        timeout=3.0, 
        event=None,
        skin=None,
    ):        
        self.timer.cancel()
        if osdText.strip() == "":
            w = 0
            h = 0
            self.bitmap = wx.EmptyBitmap(0, 0)
            self.SetPosition((-10000, -10000))
            self.Hide()
            SetEvent(event)
            return

        #self.Freeze()
        memoryDC = wx.MemoryDC()

        # make sure the mask colour is not used by foreground or 
        # background colour
        forbiddenColours = (textColour, outlineColour)
        maskColour = (255, 0, 255)
        if maskColour in forbiddenColours:
            maskColour = (0, 0, 2)
            if maskColour in forbiddenColours:
                maskColour = (0, 0, 3)
        maskBrush = wx.Brush(maskColour, wx.SOLID)
        memoryDC.SetBackground(maskBrush)

        if fontInfo is None:
            fontInfo = DEFAULT_FONT_INFO
        font = wx.FontFromNativeInfoString(fontInfo)
        memoryDC.SetFont(font)
        
        textLines = osdText.splitlines()
        sizes = [memoryDC.GetTextExtent(line or " ") for line in textLines]
        textWidths, textHeights = zip(*sizes)
        textWidth = max(textWidths)
        textHeight = sum(textHeights)
        
        if skin:
            bitmap = self.GetSkinnedBitmap(
                textLines, 
                textWidths, 
                textHeights, 
                textWidth,
                textHeight,
                memoryDC, 
                textColour, 
                "Default"
            )
            w, h = bitmap.GetSize()
        elif outlineColour is None:
            w, h = textWidth, textHeight
            bitmap = wx.EmptyBitmap(w, h)
            memoryDC.SelectObject(bitmap)

            # fill the DC background with the maskColour
            memoryDC.Clear() 
            
            # draw the text with the foreground colour
            memoryDC.SetTextForeground(textColour)
            DrawTextLines(memoryDC, textLines, textHeights)

            # mask the bitmap, so we can use it to get the needed
            # region of the window
            memoryDC.SelectObject(wx.NullBitmap)
            bitmap.SetMask(wx.Mask(bitmap, maskColour))
            
            # fill the anti-aliased pixels of the text with the foreground
            # colour, because the region of the window will add these
            # half filled pixels also. Otherwise we would get an ugly 
            # border with mask-coloured pixels.
            memoryDC.SetBackground(wx.Brush(textColour, wx.SOLID))
            memoryDC.SelectObject(bitmap)
            memoryDC.Clear()
            memoryDC.SelectObject(wx.NullBitmap)
        else:
            w, h = textWidth + 5, textHeight + 5
            outlineBitmap = wx.EmptyBitmap(w, h, 1)
            outlineDC = wx.MemoryDC()
            outlineDC.SetFont(font)
            outlineDC.SelectObject(outlineBitmap)
            outlineDC.Clear()
            outlineDC.SetBackgroundMode(wx.SOLID)
            DrawTextLines(outlineDC, textLines, textHeights)
            outlineDC.SelectObject(wx.NullBitmap)
            outlineBitmap.SetMask(wx.Mask(outlineBitmap))
            outlineDC.SelectObject(outlineBitmap)
            
            bitmap = wx.EmptyBitmap(w, h)
            memoryDC.SetTextForeground(outlineColour)
            memoryDC.SelectObject(bitmap)
            memoryDC.Clear()
            
            Blit = memoryDC.Blit
            WX_COPY = wx.COPY
            for x in xrange(5):
                for y in xrange(5):
                    Blit(x, y, w, h, outlineDC, 0, 0, WX_COPY, True)
            outlineDC.SelectObject(wx.NullBitmap)
            memoryDC.SetTextForeground(textColour)
            DrawTextLines(memoryDC, textLines, textHeights, 2, 2)
            memoryDC.SelectObject(wx.NullBitmap)
            bitmap.SetMask(wx.Mask(bitmap, maskColour))
                
        region = wx.RegionFromBitmap(bitmap)
        self.SetClientSize((w, h))
        _,_,w,_ = region.GetBox()
        self.SetShape(region)
        self.bitmap = bitmap
        monitorDimensions = GetMonitorDimensions()
        try:
            displayRect = monitorDimensions[displayNumber]
        except IndexError:
            displayRect = monitorDimensions[0]
        xOffset, yOffset = offset
        xFunc, yFunc = ALIGNMENT_FUNCS[alignment]
        x = displayRect.x + xFunc((displayRect.width - w), xOffset)
        y = displayRect.y + yFunc((displayRect.height - h), yOffset)
        self.Show()
        BringWindowToTop(self.GetHandle())
        self.SetPosition((x, y))
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bitmap, 0, 0, False)

        if timeout > 0.0:
            self.timer = threading.Timer(timeout, self.OnTimeout)
            self.timer.start()
        wx.Yield()
        SetEvent(event)
        

    def GetOutlinedBitmap(
        self, 
        textLines,                 
        textWidths, 
        textHeights, 
        textWidth,
        textHeight,
        memoryDC,
        textColour, 
        outlineColour, 
    ):
        w, h = textWidth + 5, textHeight + 5
        outlineBitmap = wx.EmptyBitmap(w, h, 1)
        outlineDC = wx.MemoryDC()
        outlineDC.SetFont(font)
        outlineDC.SelectObject(outlineBitmap)
        outlineDC.Clear()
        outlineDC.SetBackgroundMode(wx.SOLID)
        DrawTextLines(outlineDC, textLines, textHeights)
        outlineDC.SelectObject(wx.NullBitmap)
        outlineBitmap.SetMask(wx.Mask(outlineBitmap))
        outlineDC.SelectObject(outlineBitmap)
        
        bitmap = wx.EmptyBitmap(w, h)
        memoryDC.SetTextForeground(outlineColour)
        memoryDC.SelectObject(bitmap)
        memoryDC.Clear()
        
        Blit = memoryDC.Blit
        WX_COPY = wx.COPY
        for x in xrange(5):
            for y in xrange(5):
                Blit(x, y, w, h, outlineDC, 0, 0, WX_COPY, True)
        outlineDC.SelectObject(wx.NullBitmap)
        memoryDC.SetTextForeground(textColour)
        DrawTextLines(memoryDC, textLines, textHeights, 2, 2)
        memoryDC.SelectObject(wx.NullBitmap)
        bitmap.SetMask(wx.Mask(bitmap, maskColour))
        return bitmap
    
    
    def GetSkinnedBitmap(
        self, 
        textLines,                 
        textWidths, 
        textHeights, 
        textWidth,
        textHeight,
        memoryDC, 
        textColour, 
        skinName
    ):
        image = wx.Image(join(SKIN_DIR, skinName + ".png"))        
        o = eg.Bunch()
        
        def Setup(minWidth, minHeight, xMargin, yMargin, transparentColour):
            width = textWidth + 2 * xMargin
            if width < minWidth:
                width = minWidth
            height = textHeight + 2 * yMargin
            if height < minHeight:
                height = minHeight
            o.xMargin = xMargin
            o.yMargin = yMargin
            o.transparentColour = transparentColour
            bitmap = wx.EmptyBitmap(width, height)
            o.bitmap = bitmap
            memoryDC.SelectObject(bitmap)
            return width, height
            
        def Copy(x, y, w, h, toX, toY):
            bmp = wx.BitmapFromImage(image.GetSubImage((x, y, w, h)))
            memoryDC.DrawBitmap(bmp, toX, toY)
            
        def Scale(x, y, w, h, toX, toY, toW, toH):
            subImage = image.GetSubImage((x, y, w, h))
            subImage.Rescale(toW, toH, wx.IMAGE_QUALITY_HIGH)
            bmp = wx.BitmapFromImage(subImage)
            memoryDC.DrawBitmap(bmp, toX, toY)
            
        scriptGlobals = dict(Setup=Setup, Copy=Copy, Scale=Scale)
        execfile(join(SKIN_DIR, skinName + ".py"), scriptGlobals)
        
        bitmap = o.bitmap
        memoryDC.SelectObject(wx.NullBitmap)
        bitmap.SetMask(wx.Mask(bitmap, o.transparentColour))
        memoryDC.SelectObject(bitmap)
        memoryDC.SetTextForeground(textColour)
        memoryDC.SetTextBackground(textColour)
        DrawTextLines(memoryDC, textLines, textHeights, o.xMargin, o.yMargin)
        memoryDC.SelectObject(wx.NullBitmap)
        return bitmap
    
    
    def OnTimeout(self):
        self.SetPosition((-10000, -10000))
        self.Hide()
        
        
    @eg.LogIt
    def OnPaint(self, evt=None):
        wx.BufferedPaintDC(self, self.bitmap)


    if eg.debugLevel:
        @eg.LogIt
        def __del__(self):
            pass
        
     
    
class ShowOSD(eg.ActionClass):
    name = "Show OSD"
    description = "Shows a simple On Screen Display."
    iconFile = "icons/ShowOSD"
    class text:
        label = "Show OSD: %s"
        editText = "Text to display:"
        osdFont = "Text Font:"
        osdColour = "Text Colour:"
        outlineFont = "Outline OSD"
        alignment = "Alignment:"
        alignmentChoices = [
            "Top Left", 
            "Top Right", 
            "Bottom Left",
            "Bottom Right", 
            "Screen Center",
            "Bottom Center",
            "Top Center",
            "Left Center",
            "Right Center",
        ]
        display = "Show on display:"
        xOffset = "Horizontal offset X:"
        yOffset = "Vertical offset Y:"
        wait1 = "Autohide OSD after"
        wait2 = "seconds (0 = never)"
        skin = "Use skin"

    
    @classmethod
    def OnAddAction(self):
        def makeOSD():
            self.osdFrame = OSDFrame(None)
            def closeOSD():
                self.osdFrame.timer.cancel()
                self.osdFrame.Close()
            eg.app.onExitFuncs.append(closeOSD)
        wx.CallAfter(makeOSD)
        

    @eg.LogIt
    def OnClose(self):
        #self.osdFrame.timer.cancel()
        #wx.CallAfter(self.osdFrame.Close)
        self.osdFrame = None
        
        
    def __call__(
        self, 
        osdText="", 
        fontInfo=None,
        foregroundColour=(255, 255, 255), 
        backgroundColour=(0, 0, 0),
        alignment=0, 
        offset=(0, 0), 
        displayNumber=0, 
        timeout=3.0,
        skin=None
    ):
                
        self.osdFrame.timer.cancel()
        osdText = eg.ParseString(osdText)
        event = CreateEvent(None, 0, 0, None)
        wx.CallAfter(
            self.osdFrame.ShowOSD, 
            osdText, 
            fontInfo, 
            foregroundColour,
            backgroundColour, 
            alignment,
            offset, 
            displayNumber, 
            timeout, 
            event,
            skin
        )
        eg.actionThread.WaitOnEvent(event)


    def GetLabel(self, osdText, *args):
        return self.text.label % osdText.replace("\n", r"\n")
    
    
    def Configure(
        self, 
        osdText="", 
        fontInfo=None,
        foregroundColour=(255, 255, 255), 
        backgroundColour=(0, 0, 0),
        alignment=0, 
        offset=(0, 0), 
        displayNumber=0, 
        timeout=3.0,
        skin=None,
    ):                   
        if fontInfo is None:
            fontInfo = DEFAULT_FONT_INFO
        panel = eg.ConfigPanel(self)
        text = self.text
        editTextCtrl = panel.TextCtrl("\n\n", style=wx.TE_MULTILINE)
        w, h = editTextCtrl.GetBestSize()
        editTextCtrl.ChangeValue(osdText)
        editTextCtrl.SetMinSize((-1, h))
        alignmentChoice = panel.Choice(alignment, choices=text.alignmentChoices)
        displayChoice = eg.DisplayChoice(panel, displayNumber)
        xOffsetCtrl = panel.SpinIntCtrl(offset[0], -32000, 32000)
        yOffsetCtrl = panel.SpinIntCtrl(offset[1], -32000, 32000)
        timeCtrl = panel.SpinNumCtrl(timeout)
        
        fontButton = panel.FontSelectButton(fontInfo)
        foregroundColourButton = panel.ColourSelectButton(foregroundColour)
        
        if backgroundColour is None:
            tmpColour = (0,0,0)
        else:
            tmpColour = backgroundColour
        outlineCheckBox = panel.CheckBox(backgroundColour is not None, text.outlineFont)
        
        backgroundColourButton = panel.ColourSelectButton(tmpColour)
        if backgroundColour is None:
            backgroundColourButton.Enable(False)
        skinCtrl = panel.CheckBox(bool(skin), text.skin)
        
        sizer = wx.GridBagSizer(5, 5)
        EXP = wx.EXPAND
        ACV = wx.ALIGN_CENTER_VERTICAL
        Add = sizer.Add
        Add(wx.StaticText(panel, -1, text.editText), (0, 0), flag=ACV)
        Add(editTextCtrl, (0, 1), (1, 4), flag=EXP)
        
        Add(panel.StaticText(text.osdFont), (1, 3), flag=ACV)
        Add(fontButton, (1, 4))
        
        Add(panel.StaticText(text.osdColour), (2, 3), flag=ACV)
        Add(foregroundColourButton, (2, 4))

        Add(outlineCheckBox, (3, 3), flag=EXP)
        Add(backgroundColourButton, (3, 4))
        Add(skinCtrl, (4, 3))
        
        Add(panel.StaticText(text.alignment), (1, 0), flag=ACV)
        Add(alignmentChoice, (1, 1), flag=EXP)
        Add(panel.StaticText(text.display), (2, 0), flag=ACV)
        Add(displayChoice, (2, 1), flag=EXP)
        
        Add(panel.StaticText(text.xOffset), (3, 0), flag=ACV)
        Add(xOffsetCtrl, (3, 1), flag=EXP)
        
        Add(panel.StaticText(text.yOffset), (4, 0), flag=ACV)
        Add(yOffsetCtrl, (4, 1), flag=EXP)
        
        Add(panel.StaticText(text.wait1), (5, 0), flag=ACV)
        Add(timeCtrl, (5, 1), flag=EXP)
        Add(panel.StaticText(text.wait2), (5, 2), (1, 3), flag=ACV)
            
        sizer.AddGrowableCol(2)
        panel.sizer.Add(sizer, 1, wx.EXPAND)
        
        def OnCheckBox(event):
            backgroundColourButton.Enable(outlineCheckBox.IsChecked())
            event.Skip()
            
        outlineCheckBox.Bind(wx.EVT_CHECKBOX, OnCheckBox)
        
        while panel.Affirmed():
            if outlineCheckBox.IsChecked():
                outlineColour = backgroundColourButton.GetValue()
            else:
                outlineColour = None
            panel.SetResult(
                editTextCtrl.GetValue(),
                fontButton.GetValue(), 
                foregroundColourButton.GetValue(), 
                outlineColour,
                alignmentChoice.GetValue(),
                (xOffsetCtrl.GetValue(), yOffsetCtrl.GetValue()),
                displayChoice.GetValue(),
                timeCtrl.GetValue(),
                skinCtrl.GetValue()
            )
        
        