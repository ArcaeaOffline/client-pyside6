import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Dialog {
    id: root

    required property string databaseUrl

    padding: 10

    title: qsTr('Confirm Database Connection')
    standardButtons: Dialog.Ok | Dialog.Cancel
    modal: true
    Overlay.modal: Rectangle {
        color: Qt.alpha('gray', 0.2)
    }

    ColumnLayout {
        Label {
            text: 'The connection below will be saved to settings. Confirm?'
        }

        Pane {
            Label {
                id: databaseUrlLabel
                text: root.databaseUrl
            }
        }
    }
}
