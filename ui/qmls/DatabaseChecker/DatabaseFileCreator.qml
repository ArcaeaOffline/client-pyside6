import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import "../Components"

ColumnLayout {
    id: root

    signal confirm

    required property url directoryUrl
    required property string filename

    GridLayout {
        columns: 2

        Label {
            text: "Directory"
        }

        DirectorySelector {
            Layout.fillWidth: true

            directoryUrl: root.directoryUrl
            onDirectoryUrlChanged: {
                root.directoryUrl = this.directoryUrl;
            }
        }

        Label {
            text: "Filename"
        }

        TextField {
            Layout.fillWidth: true

            text: root.filename
            placeholderText: 'Please enter…'
            onEditingFinished: {
                root.filename = this.text;
            }
            onAccepted: {
                confirmButton.click();
            }
        }
    }

    Button {
        id: confirmButton
        Layout.alignment: Qt.AlignRight

        text: 'Confirm'
        onClicked: root.confirm()
    }
}
