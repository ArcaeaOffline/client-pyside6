import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "./DatabaseChecker" as DatabaseChecker

ApplicationWindow {
    visible: true

    width: 800
    height: 600

    SystemPalette {
        id: systemPaletteActive
        colorGroup: SystemPalette.Active
    }

    SystemPalette {
        id: systemPaletteDisabled
        colorGroup: SystemPalette.Disabled
    }

    palette {
        accent: systemPaletteActive.accent
        alternateBase: systemPaletteActive.alternateBase
        base: systemPaletteActive.base
        button: systemPaletteActive.button
        buttonText: systemPaletteActive.buttonText
        dark: systemPaletteActive.dark
        highlight: systemPaletteActive.highlight
        highlightedText: systemPaletteActive.highlightedText
        light: systemPaletteActive.light
        mid: systemPaletteActive.mid
        midlight: systemPaletteActive.midlight
        placeholderText: systemPaletteActive.placeholderText
        shadow: systemPaletteActive.shadow
        text: systemPaletteActive.text
        window: systemPaletteActive.window
        windowText: systemPaletteActive.windowText

        disabled {
            button: systemPaletteDisabled.button
            buttonText: systemPaletteDisabled.buttonText
        }

        inactive {
            button: systemPaletteDisabled.button
            buttonText: systemPaletteDisabled.buttonText
        }
    }

    StackLayout {
        id: stackLayout
        anchors.fill: parent
        currentIndex: 0

        DatabaseChecker.Index {
            onReady: parent.currentIndex = 1
        }

        AppMain {}
    }
}
