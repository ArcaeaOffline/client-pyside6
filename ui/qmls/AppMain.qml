pragma ComponentBehavior: Bound
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

RowLayout {
    id: layout
    spacing: 5

    SystemPalette {
        id: systemPalette
    }

    ListModel {
        id: navListModel

        ListElement {
            _id: 'home'
            label: 'Overview'
            qmlSource: 'Overview.qml'
        }
        ListElement {
            _id: 'database'
            label: 'Database'
            qmlSource: '404.qml'
        }
    }

    ListView {
        id: navListView

        Layout.preferredWidth: 200
        Layout.fillHeight: true

        model: navListModel
        focus: true

        delegate: Item {
            id: navListItem
            required property int index
            required property string label

            property bool isActive: navListView.currentIndex === index

            width: parent.width
            height: 30

            MouseArea {
                anchors.fill: parent
                onClicked: () => {
                    navListView.currentIndex = navListItem.index;
                }
            }

            Label {
                anchors.margins: 5
                anchors.fill: parent

                text: parent.label
                color: parent.isActive ? systemPalette.highlightedText : systemPalette.text
                z: 10

                Behavior on color {
                    ColorAnimation {
                        duration: 150
                    }
                }
            }

            Rectangle {
                width: parent.isActive ? parent.width : 0
                Behavior on width {
                    NumberAnimation {
                        easing.type: Easing.OutQuad
                        duration: 200
                    }
                }

                height: parent.height
                color: systemPalette.highlight
                z: 1
            }
        }
    }

    Loader {
        Layout.preferredWidth: 500
        Layout.fillWidth: true
        Layout.fillHeight: true

        source: navListView.currentIndex > -1 ? navListModel.get(navListView.currentIndex).qmlSource : '404.qml'
    }
}
