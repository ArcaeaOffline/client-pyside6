import QtQuick
import QtQuick.Layouts

RowLayout {
    id: layout
    spacing: 5

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
            required property int index
            required property string label
            width: parent.width
            height: 30

            MouseArea {
                anchors.fill: parent
                onClicked: () => {
                    navListView.currentIndex = index;
                }
            }

            Text {
                anchors.margins: 5
                anchors.fill: parent

                text: parent.label
            }
        }

        highlight: Rectangle {
            width: parent.width
            height: 30
            color: "#FFFF88"
            y: ListView.view.currentItem.y
        }
    }

    Loader {
        Layout.preferredWidth: 500
        Layout.fillWidth: true
        Layout.fillHeight: true

        source: navListView.currentIndex > -1 ? navListModel.get(navListView.currentIndex).qmlSource : '404.qml'
    }
}
