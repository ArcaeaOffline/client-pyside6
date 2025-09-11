import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Dialog {
    id: root

    required property string errorTitle
    required property string errorMessage

    padding: 10

    title: qsTr('Error')
    standardButtons: Dialog.Ok
    modal: true
    Overlay.modal: Rectangle {
        color: Qt.alpha('darkgray', 0.5)
    }

    ColumnLayout {
        spacing: 5

        Label {
            font.pointSize: 12
            font.bold: true

            text: root.errorTitle
        }

        Label {
            text: root.errorMessage
        }
    }
}
