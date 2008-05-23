﻿# -*- coding: UTF-8 -*-
class General:
    apply = u"Ü&bernehmen"
    autostartItem = u"Autostart"
    browse = u"Suchen..."
    cancel = u"Abbrechen"
    choose = u"Auswählen"
    configTree = u"Konfigurations-Baum"
    deleteLinkedItems = u"Wenigstens ein Element außerhalb der momentanen Selektion verweist auf ein Element innerhalb der zu löschenden Selektion. Wenn sie diese Selektion löschen, wird das verweisende Element nicht mehr richtig funktionieren.\n\nSind sie sicher, dass sie die Selektion löschen wollen?"
    deleteManyQuestion = u"Dieses Element hat %s Unterelemente.\n\nSollen wirklich alle gelöscht werden?"
    deletePlugin = u"Dieses Plugin wird von Befehlen in ihrer aktuellen Konfiguration benutzt.\n\nSie können es erst entfernen, wenn alle Befehle die dieses Plugin benutzen\nvorher ebenfalls entfernt wurden."
    deleteQuestion = u"Soll dieses Element wirklich gelöscht werden?"
    help = u"&Hilfe"
    moreTag = u"mehr..."
    noOptionsAction = u"Diese Aktion hat keine einstellbaren Optionen."
    noOptionsPlugin = u"Dieses Plugin hat keine einstellbaren Optionen."
    ok = u"Ok"
    pluginLabel = u"Plugin: %s"
    test = u"&Test"
    unnamedEvent = u"<Unbenanntes Ereignis>"
    unnamedFile = u"<Unbenannte Datei>"
    unnamedFolder = u"<Unbenannter Ordner>"
    unnamedMacro = u"<Unbenanntes Makro>"
class MainFrame:
    onlyLogAssigned = u"Nur &zugewiesene und aktivierte Ereignisse aufzeichnen"
    class Logger:
        caption = u"Log"
        descriptionHeader = u"Beschreibung"
        timeHeader = u"Zeit"
        welcomeText = u"---> Willkommen beim EventGhost <---"
    class Menu:
        About = u"&Über EventGhost..."
        AddPlugin = u"&Plugin hinzufügen"
        Apply = u"Änderungen &anwenden"
        CheckUpdate = u"Auf neuere Version prüfen..."
        ClearLog = u"Log löschen"
        Close = u"S&chließen"
        CollapseAll = u"Alle einklappen"
        ConfigurationMenu = u"&Konfiguration"
        Copy = u"&Kopieren"
        Cut = u"&Ausschneiden"
        Delete = u"&Löschen"
        Disabled = u"Element &deaktivieren"
        Configure = u"Element &konfigurieren"
        EditMenu = u"&Bearbeiten"
        Execute = u"Element &ausführen"
        Exit = u"&Beenden"
        ExpandAll = u"Alle ausklappen"
        ExpandOnEvents = u"Autom. markieren bei Ereignis"
        ExpandTillMacro = u"Autom. nur bis Makro ausklappen"
        Export = u"Exportieren..."
        FileMenu = u"&Datei"
        Find = u"S&uchen..."
        FindNext = u"&Weitersuchen"
        HelpMenu = u"&Hilfe"
        HideShowToolbar = u"Symbolleiste"
        Import = u"Importieren..."
        LogActions = u"Auch Befehle aufzeichnen"
        LogMacros = u"Auch Makros aufzeichnen"
        LogTime = u"Auch Zeiten aufzeichnen"
        New = u"&Neu"
        AddAction = u"&Befehl hinzufügen"
        AddEvent = u"&Ereignis hinzufügen"
        AddFolder = u"&Ordner hinzufügen"
        AddMacro = u"&Makro hinzufügen"
        Open = u"Ö&ffnen..."
        Options = u"&Einstellungen..."
        Paste = u"E&infügen"
        Redo = u"&Wiederholen"
        Rename = u"Element &umbenennen"
        Reset = u"Zurücksetzen"
        Save = u"&Speichern"
        SaveAs = u"Speichern &unter..."
        SelectAll = u"&Alles markieren"
        Undo = u"&Rückgängig"
        ViewMenu = u"&Ansicht"
        WebForum = u"Forum"
        WebHomepage = u"Homepage"
        WebWiki = u"Wiki"
    class SaveChanges:
        mesg = u"Die Datei wurde verändert.\n\nAktuelle Änderungen speichern?\n"
        title = u"Änderungen speichern?"
    class TaskBarMenu:
        Exit = u"Beenden"
        Hide = u"EventGhost verstecken"
        Show = u"EventGhost wiederherstellen"
    class Tree:
        caption = u"Konfiguration"
class Error:
    FileNotFound = u'Datei "%s" konnte nicht gefunden werden.'
    InAction = u'Fehler in Befehl: "%s"'
    configureError = u"Fehler beim Konfigurieren von: %s"
    pluginLoadError = u"Fehler beim Laden der Plugin-Datei %s."
    pluginNotActivated = u'Plugin "%s" ist nicht aktiviert'
    pluginStartError = u"Fehler beim Start des Plugins: %s"
class Exceptions:
    DeviceInitFailed = u"Gerät kann nicht initialisiert werden!"
    DeviceNotFound = u"Gerät nicht gefunden!"
    DeviceNotReady = u"Gerät ist nicht bereit!"
    DriverNotFound = u"Treiber nicht gefunden!"
    DriverNotOpen = u"Kann den Treiber nicht öffnen!"
    InitFailed = u"Initialisierung fehlgeschlagen!"
    PluginNotFound = u"Plugin nicht gefunden!"
    ProgramNotFound = u"Programm nicht gefunden!"
    ProgramNotRunning = u"Programm ist nicht gestartet!"
    SerialOpenFailed = u"Kann den seriellen Anschluss nicht öffnen!"
class CheckUpdate:
    ManErrorMesg = u"Es konnte nicht festgestellt werden, ob es eine neuere Version von EventGhost gibt.\n\nBitte versuchen sie es später noch einmal."
    ManErrorTitle = u"Fehler bei der Überprüfung"
    ManOkMesg = u"Es ist keine neuere Version von EventGhost verfügbar."
    ManOkTitle = u"Keine neuere Version verfügbar"
    downloadButton = u"Download-Seite besuchen"
    newVersionMesg = u"Eine neuere Version von EventGhost wurde veröffentlicht.\n\n	Diese Version:		%s\n	Aktuellste Version:	%s\n\nWollen Sie die Download-Seite besuchen?"
    title = u"Neuere EventGhost-Version verfügbar..."
    waitMesg = u"Bitte warten sie während EventGhost die Update-Informationen bezieht."
class AddActionDialog:
    descriptionLabel = u"Beschreibung"
    title = u"Befehl auswählen..."
class AddPluginDialog:
    author = u"Autor:"
    descriptionBox = u"Beschreibung"
    externalPlugins = u"Steuerung externer Geräte"
    noInfo = u"Keine Information verfügbar."
    noMultiload = u"Dieses Plugin unterstützt kein Mehrfachladen und\nSie haben schon eine Instanz dieses Plugins in ihrer Konfiguration."
    noMultiloadTitle = u"Mehrfachladen nicht möglich"
    otherPlugins = u"Sonstige"
    programPlugins = u"Programmsteuerung"
    remotePlugins = u"Fernbedienungsempfänger"
    title = u"Plugin hinzufügen..."
    version = u"Version:"
class AddActionGroupDialog:
    caption = u"Befehle hinzufügen?"
    message = u"EventGhost kann einen Ordner mit allen Befehlen dieses Plugins dem Konfigurationsbaum hinzufügen. Wenn Sie dieses wollen, selektieren Sie bitte unten die Stelle an dem dies geschehen soll und drücken die OK-Schaltfläche.\n\nAnsonsten drücken Sie bitte die Abbrechen-Schaltfläche."
class OptionsDialog:
    CheckUpdate = u"Auf neuere Version prüfen beim Programmstart"
    HideOnClose = u"Minimiere wenn Schließen-Schaltfläche gedrückt wird"
    HideOnStartup = u"Minimiert starten"
    LanguageGroup = u"Sprache"
    StartGroup = u"Beim Start"
    StartWithWindows = u"Automatisch mit Windows starten"
    Tab1 = u"Allgemein"
    Title = u"Einstellungen"
    UseAutoloadFile = u"Lade Datei beim Start:"
    Warning = u"Änderung der Sprache werden erst nach einem Neustart der Applikation wirksam."
    confirmDelete = u"Zeige Warnhinweis beim Löschen von Elementen"
    limitMemory1 = u"Begrenze Speicherverbrauch wenn minimiert auf"
    limitMemory2 = u"MB"
class FindDialog:
    caseSensitive = u"Groß-/Kleins&chreibung beachten"
    direction = u"Suchrichtung"
    down = u"Nach &unten"
    findButton = u"&Weitersuchen"
    notFoundMesg = u'"%s" kann nicht gefunden werden.'
    searchLabel = u"&Suchen nach:"
    searchParameters = u"Auch &Parameter von Aktionen durchsuchen"
    title = u"Suchen"
    up = u"Nach &oben"
    wholeWordsOnly = u"Nu&r ganzes Wort suchen"
class AboutDialog:
    Author = u"Autor: %s"
    CreationDate = u"%a, %d %b %Y %H:%M:%S"
    Title = u"Über EventGhost"
    Version = u"Version: %s (build %s)"
    tabAbout = u"Über EventGhost"
    tabChangelog = u"Versionshistorie"
    tabLicense = u"Lizenzabkommen"
    tabSpecialThanks = u"Besonderer Dank"
    tabSystemInfo = u"System Information"
class Plugin:
    class EventGhost:
        name = u"EventGhost"
        description = u"Diese Aktionen betreffen hauptsächlich die Kern-Funktionen von EventGhost."
        class AutoRepeat:
            name = u"Automatische Wiederholung"
            description = u"Ein Makro, dem dieser Befehl hinzugefügt wurde, wird solange wiederholt, wie die auslösende Taste gedrückt gehalten wird."
            seconds = u"Sekunden"
            text1 = u"Beginne erste Wiederholung nach"
            text2 = u"mit einer Wiederholung alle"
            text3 = u"Beschleunige Wiederholungen innerhalb von"
            text4 = u"auf eine Wiederholung alle"
        class Comment:
            name = u"Beschreibung"
            description = u"Ein Befehl der nichts tut, aber zur Kommentierung der Konfiguration benutzt werden kann."
        class DisableItem:
            name = u"Deaktiviere ein Element"
            description = u"Deaktiviere ein Element"
            label = u"Deaktiviere: %s"
            text1 = u"Bitte wählen Sie das zu deaktivierende Element:"
        class EnableExclusive:
            name = u"Aktiviere exklusiv Ordner/Makro"
            description = u"Aktiviert einen Ordner oder ein Makro, wobei gleichzeitig alle anderen Ordner/Makros, die auf der gleichen Baumebene liegen, deaktiviert werden."
            label = u"Aktiviere exklusiv: %s"
            text1 = u"Bitte wählen Sie das exklusiv zu aktivierende Element:"
        class EnableItem:
            name = u"Aktiviere ein Element"
            description = u"Aktiviere ein Element"
            label = u"Aktiviere: %s"
            text1 = u"Bitte wählen Sie das zu aktivierende Element:"
        class FlushEvents:
            name = u"Verwerfe alle ausstehenden Ereignisse"
            description = u'Diese Aktion verwirft alle Ereignisse die sich momentan in der Verarbeitungsschlange befinden.\n\nDieses ist nützlich, wenn ein Makro eine ziemlich lange Zeit zum Verarbeiten braucht und sich Ereignisse innherhalb dieser Zeit angesammelt haben, die nicht verarbeitet werden sollen.\n\n<p><b>Beispiel:</b> Sie haben ein lang andauerndes "Starte System" Makro, welches ca. 90 Sekunden braucht um z.B. einen Projektor anzuschalten und dann verschiedene Programme zu starten. Der Benutzer wird von dieser Ausführung nichts sehen, bis endlich der Projektor ein Bild zeigt und daher u.U. aus Ungeduld die auslösende Taste mehrfach drücken, was dazu führen würde, dass diese lange Verarbeitung wieder und wieder gestartet wird. Um dieses zu verhindern, können Sie die "Verwerfe alle ausstehenden Ereignisse" Aktion an das Ende Ihres Makros stellen, wodurch die überflüssigen Tastendruck-Wiederholungen entfernt werden.'
        class JumpIf:
            name = u"Springe wenn"
            description = u"Springt zu einem anderen Makro, wenn die angegebene Python-Bedingung zutrifft."
            label1 = u"Wenn %s, springe zu %s"
            label2 = u"Wenn %s, springe zu %s und kehre zurück"
            mesg1 = u"Makro wählen..."
            mesg2 = u"Bitte wählen Sie das Makro aus, welches ausgeführt werden soll, wenn die Bedingung zutrifft."
            text1 = u"Wenn:"
            text2 = u"Gehe zu:"
            text3 = u"Kehere zurück nach Ausführung"
        class JumpIfLongPress:
            name = u"Wenn langer Tastendruck"
            description = u"Springt zu einem anderen Makro, wenn die auslösende Taste länger als die eingestellte Zeit gedrückt wird."
            label = u"Wenn Tastendruck länger als %s s, gehe zu: %s"
            text1 = u"Wenn die Taste länger als"
            text2 = u"Sekunden gedrückt wird, springe zu dem"
            text3 = u"Makro:"
            text4 = u"Makro auswählen..."
            text5 = u"Bitte wählen Sie das Makro, welches bei einem langen\nTastendruck angesprungen werden soll."
        class NewJumpIf:
            name = u"Sprungbefehl"
            description = u"Springt zu einem anderen Makro, wenn die angegebene Bedingung zutrifft."
            choices = [
                u"letzter Befehl erfolgreich",
                u"letzter Befehl nicht erfolgreich",
                u"Immer",
            ]
            labels = [
                u'Wenn erfolgreich springe zu "%s"',
                u'Wenn erfolglos springe zu "%s"',
                u'Springe zu "%s"',
                u'Wenn erfolgreich springe zu "%s" und kehre zurück',
                u'Wenn erfolglos springe zu "%s" und kehre zurück',
                u'Springe zu "%s" und kehre zurück',
            ]
            mesg1 = u"Wähle Makro..."
            mesg2 = u"Bitte wählen sie das Makro, welches ausgeführt werden soll, wenn die Bedingung zutrifft."
            text1 = u"Wenn:"
            text2 = u"Springe zu:"
            text3 = u"und kehre zurück nach der Ausführung"
        class PythonCommand:
            name = u"Python Befehl"
            description = u"Führt das angegebene Parameter als einzeiligen Python-Befehl aus."
            parameterDescription = u"Python Anweisung:"
        class PythonScript:
            name = u"Python Skript"
            description = u"Über diesen Befehl können Python Skripte erzeugt werden, die alle Möglichkeiten der Programmiersprache Python bieten."
        class ShowOSD:
            name = u"Zeige OSD"
            description = u'Zeigt einen einfaches "On Screen Display"'
            alignment = u"Ausrichtung:"
            alignmentChoices = [
                u"oben links",
                u"oben rechts",
                u"unten links",
                u"unten rechts",
                u"mittig",
                u"mittig unten",
                u"mittig oben",
                u"mittig links",
                u"mittig rechts",
            ]
            display = u"Zeige auf Monitor:"
            editText = u"Darzustellender Text:"
            label = u"Zeige OSD: %s"
            osdColour = u"OSD Farbe:"
            osdFont = u"OSD Zeichensatz:"
            outlineFont = u"Umrandungsfarbe"
            skin = u"Benutze Skin"
            wait1 = u"Blende OSD nach"
            wait2 = u"Sekunden automatisch aus. (0 = nicht ausblenden)"
            xOffset = u"Horizontaler Versatz X:"
            yOffset = u"Vertikaler Versatz Y:"
        class StopIf:
            name = u"Stoppe wenn"
        class StopProcessing:
            name = u"Beende Bearbeitung dieses Ereignisses"
            description = u"Wird dieser Befehl ausgeführt, dann sucht EventGhost nicht mehr nach weiteren Makros, die zu dem aktuellen Ereignis passen würden."
        class TriggerEvent:
            name = u"Erzeuge Ereignis"
            description = u"Erzeugt ein neues Ereignis (optional nach einiger Zeit)."
            labelWithTime = u'Erzeuge Ereignis "%s" nach %.2f Sekunden'
            labelWithoutTime = u'Erzeuge Ereignis "%s"'
            text1 = u"Zu erzeugender Ereignis-Name:"
            text2 = u"Verzögere das Ereignis um:"
            text3 = u"Sekunden. (0 = erzeuge sofort)"
        class Wait:
            name = u"Warte"
            description = u"Unterbricht die Ausführung des Makros für eine angegebene Zeit, bevor der nächste Befehl ausgeführt wird."
            label = u"Warte: %s s"
            seconds = u"Sekunden"
            wait = u"Warte"
    class System:
        name = u"System"
        description = u"Diese Aktionen steuern verschiedene Eigenschaften des Betriebssystems."
        forced = u"Erzwungen: %s"
        forcedCB = u"Erzwinge Schließung aller Programme"
        class ChangeDisplaySettings:
            name = u"Ändere Anzeige-Einstellungen"
            description = u"Anzeige-Eigenschaften ändern"
            colourDepth = u"Farbtiefe:"
            display = u"Bildschirm:"
            frequency = u"Bildschirmfrequenz:"
            includeAll = u"Modi anzeigen, die von dieser Monitor unter Umständen nicht unterstützt werden."
            label = u"Setze Anzeige %d auf %dx%d@%d Hz"
            resolution = u"Auflösung:"
            storeInRegistry = u"Speichere Einstellung in der Registry."
        class ChangeMasterVolumeBy:
            name = u"Verändere Master-Lautstärke"
            description = u"Ändert die Gesamtlautstärke relativ."
            text1 = u"Verändere Master-Lautstärke um"
            text2 = u"Prozent."
        class Execute:
            name = u"Starte Anwendung"
            description = u"Startet eine ausführbare Datei."
            FilePath = u"Pfad zur ausführbaren Datei:"
            Parameters = u"Aufruf-Parameter:"
            ProcessOptions = (
                u"Echtzeit",
                u"Höher als normal",
                u"Normal",
                u"Niedriger als normal",
                u"Niedrig",
            )
            ProcessOptionsDesc = u"Prozess Priorität:"
            WaitCheckbox = u"Auf Beendigung des Programmes warten bevor fortgeschritten wird."
            WindowOptions = (
                u"Normal",
                u"Minimiert",
                u"Maximiert",
                u"Versteckt",
            )
            WindowOptionsDesc = u"Fenster-Optionen:"
            WorkingDir = u"Startverzeichnis:"
            browseExecutableDialogTitle = u"Wählen sie die ausführbare Datei"
            browseWorkingDirDialogTitle = u"Wählen sie das Arbeitsverzeichnis"
            label = u"Starte Anwendung: %s"
        class Hibernate:
            name = u"Ruhezustand"
            description = u"Wenn der Computer in den Ruhezustand wechselt, wird der Inhalt des Arbeitsspeichers gespeichert und der Computer wird heruntergefahren. Wenn er wieder gestartet wird, kehrt er zum vorherigen Zustand zurück. (Hibernation/S4)"
        class LockWorkstation:
            name = u"Computer sperren"
            description = u'Dieser Befehl sendet eine Anforderung and das System den Bildschirm zu sperren. Den Computer zu sperren schützt ihn vor unbefugtem Zugriff. Dieser Befehl führt zu dem gleichen Ergebnis wie das Drücken von Ctrl+Alt+Del und das anschließende Klicken auf "Computer sperren".'
        class LogOff:
            name = u"Benutzer abmelden"
            description = u"Beendet alle Programme in der aktuellen Benutzeranmeldung. Anschließend wird der Benutzer abgemeldet."
        class MonitorGroup:
            name = u"Bildschirm"
            description = u"Diese Befehle steuern verschiedene Eigenschaften des Bildschirms."
        class MonitorPowerOff:
            name = u"Bildschirm ausschalten"
        class MonitorPowerOn:
            name = u"Bildschirm reaktivieren"
        class MonitorStandby:
            name = u"Bildschirm standby"
        class MuteOff:
            name = u"Stummschaltung aus"
            description = u"Deaktiviert die Stummschaltung."
        class MuteOn:
            name = u"Stummschaltung an"
            description = u"Aktiviert die Stummschaltung."
        class OpenDriveTray:
            name = u"Öffne/Schließe Laufwerksschublade"
            description = u"Ermöglicht es die Laufwerksschublade von CD und DVD-Laufwerken zu öffnen und zu schließen."
            driveLabel = u"Laufwerk:"
            labels = [
                u"Öffne/Schließe Laufwerksschublade: %s",
                u"Öffne Laufwerksschublade: %s",
                u"Schließe Laufwerksschublade: %s",
            ]
            options = [
                u"Laufwerksschublade wechselnd öffnen und schließen",
                u"Nur Laufwerksschublade öffnen",
                u"Nur Laufwerksschublade schließen",
            ]
            optionsLabel = u"Wähle Aktion"
        class PlaySound:
            name = u"Audiodatei abspielen"
            description = u"Spielt eine Audiodatei ab."
            fileMask = u"WAV-Dateien (*.WAV)|*.wav|Alle Dateien (*.*)|*.*"
            text1 = u"Pfad zur Audiodatei:"
            text2 = u"Warte auf Beendigung"
        class PowerDown:
            name = u"Rechner ausschalten"
        class PowerGroup:
            name = u"Energieoptionen"
        class Reboot:
            name = u"Rechner neu starten"
        class RegistryChange:
            name = u"Registrierungs-Wert ändern"
            description = u"Verändert einen Wert in der Windows-Registrierung"
            actions = (
                u"anlegen oder verändern",
                u"nur ändern wenn vorhanden",
                u"löschen",
            )
            labels = (
                u'Ändere "%s" zu "%s"',
                u'Ändere "%s" zu "%s" nur wenn vorhanden',
                u'Lösche "%s"',
            )
        class RegistryGroup:
            name = u"Registrierung"
            description = u"Abfrage und Änderung von Werten in der Windows-Registrierung."
            actionText = u"Aktion:"
            chooseText = u"Registrierungs-Schlüssel wählen:"
            defaultText = u"(Standard)"
            keyOpenError = u"Fehler beim Öffnen des Registrierungs-Schlüssels"
            keyText = u"Schlüssel:"
            keyText2 = u"Schlüssel"
            newValue = u"Neuer Wert"
            noKeyError = u"Kein Schlüssel angegeben"
            noNewValueError = u"Kein neuer Wert angegeben"
            noSubkeyError = u"Kein Unterschlüssel angegeben"
            noTypeError = u"Keinen Type angegeben"
            noValueNameError = u"Kein Name für den Wert angegeben"
            noValueText = u"Wert nicht gefunden"
            oldType = u"Momentaner Typ:"
            oldValue = u"Momentaner Wert:"
            typeText = u"Typ:"
            valueChangeError = u"Fehler beim Versuch den Wert zu ändern"
            valueName = u"Name:"
            valueText = u"Wert:"
        class RegistryQuery:
            name = u"Registrierungs-Wert auslesen"
            description = u"Fragt die Windows-Registrierung ab und liefert einen Wert zurück oder vergleicht ihn."
            actions = (
                u"teste auf Existenz",
                u"liefere als Resultat zurück",
                u"vergleiche mit",
            )
            labels = (
                u'Prüfe ob "%s" vorhanden',
                u'Liefere "%s" als Resultat zurück',
                u'Vergleiche "%s" mit "%s"',
            )
        class SetClipboard:
            name = u"Zeichenkette in die Zwischenablage kopieren"
            description = u"Kopiert eine als Parameter angegebene Zeichenkette in die System-Zwischenablage."
            error = u"Kann Zwischenablage nicht öffnen"
        class SetMasterVolume:
            name = u"Setze Master-Lautstärke"
            description = u"Setzt die Gesamtlautstärke auf einen absoluten Wert."
            text1 = u"Setze Master-Lautstärke auf"
            text2 = u"Prozent."
        class SetWallpaper:
            name = u"Desktop-Hintergrund wechseln"
            description = u"Wechselt das Desktop-Hintergrundbild."
            choices = (
                u"Zentriert",
                u"Nebeneinander",
                u"Gestreckt",
            )
            fileMask = u"Alle Bilddateien|*.jpg;*.bmp;*.gif|Alle Dateien (*.*)|*.*"
            text1 = u"Pfad zur Bilddatei:"
            text2 = u"Ausrichtung:"
        class ShowPicture:
            name = u"Bild anzeigen"
            allFiles = u"Alle Dateien"
            allImageFiles = u"Alle Bilddateien"
            display = u"Monitor:"
            path = u"Pfad zur Bilddatei:"
        class SoundGroup:
            name = u"Audiokarte"
            description = u"Diese Aktionen steuern die Audio-Funktionen des Computers."
        class Standby:
            name = u"Rechner standby"
        class StartScreenSaver:
            name = u"Starte Bildschirmschoner"
            description = u"Startet den momentan im Betreibssystem ausgewählten Blidschrimschoner."
        class ToggleMute:
            name = u"Stummschaltung umschalten"
            description = u"Wechselt die Stummschaltung von aktiviert auf deaktiviert und umgekehrt."
    class Window:
        name = u"Fenster"
        class BringToFront:
            name = u"Fenster nach vorne bringen"
            description = u"Bringt ein Fenster vor alle anderen Fenster des Desktops."
        class Close:
            name = u"Fenster schließen"
            description = u"Schließt Anwendungs-Fenster"
        class FindWindow:
            name = u"Finde Fenster"
            description = u'Sucht ein oder mehrere Fenster, welche dann für weitere Befehle der Fenster-Gruppe als Ziel definiert werden.\n\n<p>Wenn ein Makro keinen "Finde Fenster" Befehl besitzt, werden alle Fenster Befehle dieses Makros nur auf das vorderste Fenster zielen.\n<p>In den Textfeldern können Sie die in geschweifte Klammern gesetzten Platzhalter {*} für beliebiger Zeichenfolgen und/oder {?} für genau ein Zeichen verwenden.'
            drag1 = u"Ziehe mich auf\nein Fenster."
            drag2 = u"Nun bewege mich\nauf ein Fenster."
            hide_box = u"Verstecke EventGhost beim Ziehen"
            invisible_box = u"Auch unsichtbare Objekte durchsuchen"
            label = u"Finde Fenster: %s"
            label2 = u"Finde vorderstes Fenster"
            matchNum1 = u"Nur den Treffer Nr."
            matchNum2 = u"zurückgeben"
            onlyFrontmost = u"Nur vorderstes Fenster suchen"
            options = (
                u"Programm:",
                u"Fenster Name:",
                u"Fenster Klasse:",
                u"Unter-Fenster Name:",
                u"Unter-Fenster Klasse:",
            )
            refresh_btn = u"&Aktualisieren"
            stopMacro = [
                u"Stoppe Makro wenn Ziel nicht gefunden",
                u"Stoppe Makro wenn Ziel gefunden",
                u"Niemals Makro stoppen",
            ]
            testButton = u"Test"
            wait1 = u"Warte bis zu "
            wait2 = u"Sekunden auf das Erscheinen des Fensters."
        class Maximize:
            name = u"Fenster maximieren"
            description = u"Maximiert Fenster"
        class Minimize:
            name = u"Fenster minimieren"
            description = u"Minimiert Fenster"
        class MoveTo:
            name = u"Fenster verschieben"
            description = u"Verschiebt Fenster"
            label = u"Fenster nach %s verschieben"
            text1 = u"Setze horizontale Position X:"
            text2 = u"Pixel"
            text3 = u"Setze vertikale Position Y:"
            text4 = u"Pixel"
        class Resize:
            name = u"Fenstergröße ändern"
            description = u"Ändert die Größe eines Fensters."
            label = u"Ändere Fenstergröße auf %s, %s"
            text1 = u"Setze Breite auf"
            text2 = u"Pixel"
            text3 = u"Setze Höhe auf"
            text4 = u"Pixel"
        class Restore:
            name = u"Fenster wiederherstellen"
        class SendKeys:
            name = u"Emuliere Tastatureingabe"
            description = u'Diese Aktion emuliert Tastatureingaben, die zur Kontrolle von anderen Programmen verwendet werden können. \n\n<p>Geben Sie einfach den zu tippenden Text in die Textbox ein. Um Sondertasten zu emulieren, muss ein Schlüsselwort in geschweifte Klammern gesetzt werden.\n<p>\nFor example if you want to have a cursor-up-key you write <b>{Up}</b>. You \ncan combine multiple keywords with the plus sign to get key-combinations like \n<b>{Shift+Ctrl+F1}</b> or <b>{Ctrl+V}</b>. The keywords are not \ncase-sensitive, so you can write {SHIFT+ctrl+F1} as well if you like. \n<p>\nSome keys differentiate between the left or the right side of the keyboard \nand can then be prefixed with an "L" or "R", like the Windows-Key:<br>\n<b>{Win}</b> or <b>{LWin}</b> or <b>{RWin}</b>\n<p>\nAnd here is the list of the remaining keywords EventGhost understands:<br>\n<b>{Ctrl}</b> or <b>{Control}<br>\n{Shift}<br>\n{Alt}<br>\n{Return}</b> or <b>{Enter}<br>\n{Back}</b> or <b>{Backspace}<br>\n{Tab}</b> or <b>{Tabulator}<br>\n{Esc}</b> or <b>{Escape}<br>\n{Spc}</b> or <b>{Space}<br>\n{Up}<br>\n{Down}<br>\n{Left}<br>\n{Right}<br>\n{PgUp}</b> or <b>{PageUp}<br>\n{PgDown}</b> or <b>{PageDown}<br>\n{Home}<br>\n{End}<br>\n{Ins}</b> or <b>{Insert}<br>\n{Del}</b> or <b>{Delete}<br>\n{Pause}<br>{Capslock}<br>\n{Numlock}<br>\n{Scrolllock}<br>\n{F1}, {F2}, ... , {F24}<br>\n{Apps}</b> (This is the context-menu-key)<b><br>\n<br>\n</b>These will emulate keys from the numpad:<b><br>\n{Divide}<br>{Multiply}<br>\n{Subtract}<br>\n{Add}<br>\n{Decimal}<br>\n{Numpad0}, {Numpad1}, ... , {Numpad9}</b>\n'
            insertButton = u"&Einfügen"
            specialKeyTool = u"Sondertasten Werkzeug"
            textToType = u"Zu tippender Text:"
            useAlternativeMethod = u"Verwende alternative Methode zur Emulation von Tastatureingaben."
            class Keys:
                backspace = u"Rücktaste"
                context = u"Kontextmenü Taste"
                delete = u"Entfernen"
                down = u"Pfeiltaste nach unten"
                end = u"Ende"
                home = u"Pos1"
                insert = u"Einfügen"
                left = u"Pfeiltaste nach links"
                num0 = u"Ziffernblock 0"
                num1 = u"Ziffernblock 1"
                num2 = u"Ziffernblock 2"
                num3 = u"Ziffernblock 3"
                num4 = u"Ziffernblock 4"
                num5 = u"Ziffernblock 5"
                num6 = u"Ziffernblock 6"
                num7 = u"Ziffernblock 7"
                num8 = u"Ziffernblock 8"
                num9 = u"Ziffernblock 9"
                numAdd = u"Ziffernblock +"
                numDecimal = u"Ziffernblock Dezimaltrenner"
                numDivide = u"Ziffernblock /"
                numMultiply = u"Ziffernblock *"
                numSubtract = u"Ziffernblock -"
                pageDown = u"Bild runter"
                pageUp = u"Bild hoch"
                right = u"Pfeiltaste nach rechts"
                space = u"Leerschritt"
                up = u"Pfeiltaste nach oben"
                win = u"Windows Taste"
    class Mouse:
        name = u"Maus"
        class GoDirection:
            name = u"Starte Mausbewegung in eine Richtung"
            label = u"Starte Mausbewegung in Richtung %.2f°"
            text1 = u"Starte Mausbewegung in Richtung"
            text2 = u"Grad."
        class LeftButton:
            name = u"Linke Maustaste"
        class LeftDoubleClick:
            name = u"Linke Maustaste Doppelklick "
        class MiddleButton:
            name = u"Mittlere Maustaste"
        class MouseWheel:
            name = u"Drehe Mausrad"
            description = u"Emuliert Drehungen des Mausrades"
            label = u"Drehe Mausrad um %d Rastungen"
            text1 = u"Drehe Mausrad um"
            text2 = u"Rastungen. (Negative Werte drehen nach unten)"
        class MoveAbsolute:
            name = u"Setze Maus-Position"
            label = u"Bewege Maus nach x:%s, y:%s"
            text1 = u"Setze horizontale Position X:"
            text2 = u"Pixel"
            text3 = u"Setze vertikale Position Y:"
            text4 = u"Pixel"
        class RightButton:
            name = u"Rechte Maustaste"
        class RightDoubleClick:
            name = u"Rechte Maustaste Doppelklick"
        class ToggleLeftButton:
            name = u"Linke Maustaste umschalten"
    class Joystick:
        name = u"Joystick"
        description = u"Dieses Plugin erlaubt es Joysticks und Gamepads als Ereignisquelle zu verwenden."
    class Keyboard:
        name = u"Tastatur"
        description = u"Dieses Plugin generiert Ereignisse bei Tastendruck (Hotkey)."
    class NetworkReceiver:
        name = u"Netzwerk Ereignis Empfänger"
        description = u'Empfängt Ereignisse von einem "Netzwerk Ereignis Sender" Plugin.'
        eventPrefix = u"Ereignis Prefix:"
        password = u"Passwort:"
        port = u"Port:"
    class NetworkSender:
        name = u"Netzwerk Ereignis Sender"
        description = u'Sendet Ereignisse zu einem "Netzwerk Ereignis Empfänger" Plugin über das TCP/IP Protokoll.'
        password = u"Passwort:"
        securityBox = u"Sicherheit"
        tcpBox = u"TCP/IP Einstellungen"
    class Serial:
        name = u"Serieller Anschluss"
        description = u"Allgemeine Kommunikation über einen seriellen Anschluss."
        baudrate = u"Bits pro Sekunde:"
        bytesize = u"Datenbits:"
        encoding = u"Zeichenkodierung:"
        eventPrefix = u"Ereignis-Prefix"
        flowcontrol = u"Flusssteuerung:"
        generateEvents = u"Generiere Ereignisse bei eintreffenden Daten"
        handshakes = [
            u"Keine",
            u"Xon / Xoff",
            u"Hardware",
        ]
        parities = [
            u"Keine",
            u"Ungerade",
            u"Gerade",
        ]
        parity = u"Parität:"
        port = u"Anschluss:"
        stopbits = u"Stopbits:"
        terminator = u"Endzeichen:"
        class Read:
            name = u"Lese"
            read_all = u"Lese soviele Zeichen wie momentan verfügbar sind."
            read_some = u"Lese genau diese Anzahl an Zeichen:"
            read_time = u"und warte maximal diese Anzahl an Millisekunden auf sie:"
        class Write:
            name = u"Sende"
    class Speech:
        name = u"Sprachausgabe"
        description = u"Verwendet die Microsoft Speech API (SAPI) um Texte in Sprache zu wandeln."
        class TextToSpeech:
            name = u"Text in Sprache"
            description = u"Verwendet die Microsoft Speech API (SAPI) um Texte in Sprache zu wandeln."
            buttonInsertDate = u"Datum einfügen"
            buttonInsertTime = u"Zeit einfügen"
            errorCreate = u"Kann Sprachobjekt nicht herstellen"
            errorNoVoice = u"Die Stimme mit dem Namen %s ist nicht verfügbar"
            fast = u"Schnell"
            label = u"Spreche: %s"
            labelRate = u"Geschwindigkeit:"
            labelVoice = u"Stimme:"
            labelVolume = u"Lautstärke:"
            loud = u"Laut"
            normal = u"Normal"
            silent = u"Leise"
            slow = u"Langsam"
            textBoxLabel = u"Text"
            voiceProperties = u"Spracheigenschaften"
    class SysTrayMenu:
        name = u"System Tray Menü"
        description = u"Ermöglicht es das Tray-Menü von EventGhost um eigene Menü-Einträge zu erweitern."
        addBox = u"Hinzufügen:"
        addItemButton = u"Menüeintrag"
        addSeparatorButton = u"Trennlinie"
        deleteButton = u"Entfernen"
        editEvent = u"Ereignis:"
        editLabel = u"Beschriftung:"
        eventHeader = u"Ereignis"
        labelHeader = u"Beschriftung"
        unnamedEvent = u"Ereignis%s"
        unnamedLabel = u"Neuer Menü-Eintrag %s"
    class TestPatterns:
        name = u"Testbild"
        description = u"Ermöglicht die Anzeige einer Reihe von Testbildern."
        aspectRatio = u"Seitenverhältnis:"
        aspectRatios = [
            u"1:1 Pixel-Zuordnung",
            u"4:3 Vollbild",
            u"16:9 Vollbild",
            u"4:3 Vollbild nach ITU-R BT.601 PAL",
            u"16:9 Vollbild nach ITU-R BT.601 PAL",
        ]
        backgroundColour = u"Hintergrundfarbe:"
        coverage = u"Abdeckung (Prozent):"
        display = u"Bildschirm:"
        dotDiameter = u"Durchmesser:"
        firstColour = u"Erste Farbe:"
        foregroundColour = u"Vordergrundfarbe:"
        lastColour = u"Letzte Farbe:"
        lineSize = u"Linienstärke:"
        makeDoubleBars = u"Doppelte Balken"
        numElements = u"Elementanzahl:"
        numHorizontalElements = u"Anzahl horizontaler Elemente:"
        numVerticalElements = u"Anzahl vertikaler Elemente:"
        numberFont = u"Nummer Zeichensatz:"
        orientation = u"Ausrichtung:"
        orientations = [
            u"horizontal",
            u"vertical",
        ]
        radius1 = u"Radius:"
        radius2 = u"% (0=ganzer Bildschirm)"
        secondColour = u"Zweite Farbe:"
        showNumbers = u"Zeige Nummern"
        useAntiAlias = u"Verwende Anti-Aliasing"
        class Bars:
            name = u"Balken"
        class Checkerboard:
            name = u"Schachbrett"
        class Close:
            name = u"Schließen"
        class Dots:
            name = u"Punkte"
        class Focus:
            name = u"Fokus"
        class Geometry:
            name = u"Geometrie"
        class Grid:
            name = u"Gitter"
        class IreWindow:
            name = u"IRE Fenster"
        class Lines:
            name = u"Linien"
        class SetDisplay:
            name = u"Anzeige setzen"
        class SiemensStar:
            name = u"Siemensstern"
    class USB_UIRT:
        name = u"USB-UIRT"
        blinkRx = u"Blinke bei Empfang"
        blinkTx = u"Blinke beim Senden"
        irReception = u"IR Empfang"
        legacyCodes = u"Generiere UIRT2-kompatible Ereignisse"
        notFound = u"<unbekannt>"
        redIndicator = u"Funktion der roten Anzeige-LED"
        stopCodes = u"Akzeptiere kurze Wiederholsequenzen als fortdauernde Ereignisse"
        uuFirmDate = u"Firmware Datum: "
        uuFirmVersion = u"Firmware Version: "
        uuInfo = u"USB-UIRT Information"
        uuProtocol = u"Protokoll Version: "
        class TransmitIR:
            name = u"Sende IR"
            description = u"Sendet eine IR-Code durch das USB-UIRT Gerät."
            infinite = u"unendlich"
            irCode = u"IR-Code:"
            learnButton = u"Lerne IR-Code..."
            repeatCount = u"Wiederholungen:"
            wait1 = u"Warte auf:"
            wait2 = u"ms IR Inaktivität vor Aussendung"
            zone = u"Zone:"
            zoneChoices = (
                u"Alle",
                u"Anschlussbuchse R-Kontakt",
                u"Anschlussbuchse L-Kontakt",
                u"Interner Sender",
            )
            class LearnDialog:
                acceptBurstButton = u"Akzeptiere Signalfolge"
                forceRaw = u"Lernen im RAW-Modus erzwingen"
                frequency = u"Frequenz"
                helpText = u"1. Lassen Sie die Fernbedienung aus einer \nEntfernung von ungefähr 15 cm (oder auch weniger)\nauf die Vorderseite des USB-UIRT zeigen.\n\n2. DRÜCKEN und HALTEN Sie die gewünschte Taste\nder Fernbedienung, bis das Lernen abgeschlossen ist.\n"
                progress = u"Lern-Fortschritt"
                signalQuality = u"Signal"
                title = u"Lerne IR-Code"
    class Webserver:
        name = u"Webserver"
        description = u"Ein kleiner Webserver, mit dem Ereignisse durch HTML-Webseiten generiert werden können."
        documentRoot = u"Datenverzeichnis:"
        eventPrefix = u"Ereignis Prefix:"
        port = u"TCP/IP Port:"
    class X10:
        name = u"X10 Fernbedienung"
        description = u'Plugin für X10 kompatible Funkfernbedienungen.\n\nDies beinhaltet Fernbedienungen wie:<br>\n<ul>\n<li><a href="http://www.ati.com/products/remotewonder/index.html">ATI Remote Wonder</a></li>\n<li><a href="http://www.ati.com/products/remotewonderplus/index.html">ATI Remote Wonder™ PLUS</a></li>\n<li><a href="http://www.snapstream.com/">SnapStream Firefly</a></li>\n<li><a href="http://www.nvidia.com/object/feature_PC_remote.html">NVIDIA Personal Cinema Remote</a></li>\n<li><a href="http://www.marmitek.com/">Marmitek PC Control</a></li>\n<li><a href="http://www.pearl.de/product.jsp?pdid=PE4444&catid=1601&vid=916&curr=DEM">Pearl Q-Sonic Master Remote 6in1</a></li>\n<li>Medion RF Remote Control</li>\n</ul>\n'
        allButton = u"&Alle"
        errorMesg = u"Kein X10 Empfänger gefunden!"
        idBox = u"Aktivierte IDs:"
        noneButton = u"&Keine"
        remoteBox = u"Fernbedienungstyp:"
        usePrefix = u"Ereignis-Prefix:"