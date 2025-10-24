import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import internal.ui.vm 1.0

Page {
    id: root

    property alias b30: vm.b30

    OverviewViewModel {
        id: vm
    }

    component Display: RowLayout {
        required property string label
        required property string value

        spacing: 5

        // implicitHeight: valueText.implicitHeight

        Label {
            text: parent.label
            Layout.alignment: Qt.AlignBaseline
        }

        Label {
            id: valueText

            text: parent.value
            font.pointSize: 18
            Layout.alignment: Qt.AlignBaseline
        }
    }

    RowLayout {
        ColumnLayout {
            Layout.fillWidth: true
            Layout.alignment: Qt.AlignBottom

            Display {
                label: 'B30'
                value: root.b30 >= 0 ? root.b30.toFixed(3) : 'N/A'
            }

            Display {
                label: 'R10'
                value: 'Not supported'
            }
        }

        Button {
            Layout.alignment: Qt.AlignBottom

            // TODO: icon
            text: 'Reload'
            onClicked: vm.reload()
        }
    }
}
