import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "../Components"

ColumnLayout {
    id: root

    property alias selectFileUrl: fileSelector.url
    property alias createDirectoryUrl: fileCreator.directoryUrl
    property alias createFilename: fileCreator.filename

    signal uiModeChanged(string value)
    signal confirmCreate

    ListModel {
        id: uiModeModel
        ListElement {
            value: 'select'
        }
        ListElement {
            value: 'create'
        }
    }

    TabBar {
        id: tabBar
        Layout.fillWidth: true

        TabButton {
            text: qsTr("Select Existing")
            width: implicitWidth + 10
        }
        TabButton {
            text: qsTr("Create New File")
            width: implicitWidth + 10
        }

        onCurrentIndexChanged: {
            const idx = this.currentIndex;
            root.uiModeChanged(uiModeModel.get(idx).value);
        }
    }

    StackLayout {
        currentIndex: tabBar.currentIndex

        Layout.fillWidth: true
        Layout.preferredHeight: children[currentIndex].height
        Behavior on Layout.preferredHeight {
            PropertyAnimation {
                duration: 300
                easing.type: Easing.InOutCubic
            }
        }
        clip: true

        FileSelector {
            id: fileSelector
        }

        DatabaseFileCreator {
            id: fileCreator

            onConfirm: root.confirmCreate()
        }
    }
}
