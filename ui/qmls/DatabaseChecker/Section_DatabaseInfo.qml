import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ColumnLayout {
    id: root

    property var info: {
        'url': undefined,
        'error': {
            'title': undefined,
            'message': undefined
        },
        'initialized': undefined,
        'version': undefined
    }
    property bool showErrorDialog: false

    function hasError(): bool {
        return info?.error?.title !== undefined || info?.error?.message !== undefined;
    }

    function displayText(value): string {
        return value ?? '-';
    }

    function displayBool(value): string {
        if (value === undefined)
            return '-';
        // TODO: color success & error
        return value ? `<font color="lightgreen">Yes</font>` : `<font color="lightpink">No</font>`;
    }

    component LabelLabel: Label {
        Layout.alignment: Qt.AlignRight | Qt.AlignBaseline
        font.pointSize: 10
    }

    SystemPalette {
        id: palette
    }

    Dialog_Error {
        parent: Overlay.overlay

        anchors.centerIn: parent
        visible: root.hasError() && root.showErrorDialog

        errorTitle: root.displayText(root.info?.error?.title)
        errorMessage: root.displayText(root.info?.error?.message)

        onClosed: root.showErrorDialog = false
    }

    Pane {
        clip: true
        background: Rectangle {
            color: Qt.darker(Qt.alpha(palette.window, 0.9), 0.2)
        }

        // Layout.preferredHeight: root.hasError() ? this.implicitHeight : 0
        Layout.preferredHeight: 0
        Behavior on Layout.preferredHeight {
            PropertyAnimation {
                duration: 300
                easing.type: Easing.InOutCubic
            }
        }

        ColumnLayout {
            anchors.fill: parent

            Label {
                font.bold: true
                text: root.displayText(root.info.error?.title)
            }

            Label {
                text: root.displayText(root.info.error?.message)
            }
        }
    }

    GridLayout {
        columns: 2
        columnSpacing: 10

        LabelLabel {
            text: 'Connection'
        }

        Label {
            text: root.info.url
        }

        LabelLabel {
            text: 'Initialized'
        }

        Label {
            text: root.displayBool(root.info?.initialized)
        }

        LabelLabel {
            text: 'Version'
        }

        Label {
            text: root.displayText(root.info?.version)
        }

        Column {
            Layout.alignment: Qt.AlignRight | Qt.AlignBaseline

            LabelLabel {
                text: 'Error'
            }

            ToolButton {
                Layout.preferredWidth: root.hasError() ? this.implicitWidth : 0
                Behavior on Layout.preferredWidth {
                    PropertyAnimation {
                        duration: 300
                        easing.type: Easing.InOutCubic
                    }
                }

                text: '[?]'
                onClicked: root.showErrorDialog = true
            }
        }

        Label {
            Layout.alignment: Qt.AlignBaseline
            text: root.displayText(root.info?.error?.title)
        }
    }
}
