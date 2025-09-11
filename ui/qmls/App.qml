import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "./DatabaseChecker" as DatabaseChecker

ApplicationWindow {
    visible: true

    width: 800
    height: 600

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
