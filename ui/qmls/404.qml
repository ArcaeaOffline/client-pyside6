import QtQuick
import QtQuick.Controls

Page {
    Column {
        anchors.centerIn: parent
        width: parent.width

        Label {
            width: parent.width
            text: '?'
            font.pointSize: 50
            horizontalAlignment: Qt.AlignCenter
        }

        Label {
            width: parent.width
            text: 'Placeholder page'
            horizontalAlignment: Qt.AlignCenter
        }
    }
}
