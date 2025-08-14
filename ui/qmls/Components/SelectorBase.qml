import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import internal.ui.utils

RowLayout {
    id: root

    required property var shouldAcceptUrl  // function (url)
    signal browseButtonClicked
    property string placeholderText: '<font color="gray">…</font>'

    required property url url
    onUrlChanged: {
        Qt.callLater(() => {
            updateLabel();
        });
    }

    function updateLabel(): void {
        urlLabel.text = url.toString().length > 0 ? UrlFormatUtils.toLocalFile(url) : root.placeholderText;
    }

    spacing: 2

    Label {
        id: urlLabel
        Layout.fillWidth: true
        text: root.placeholderText

        DropArea {
            anchors.fill: parent

            onEntered: drag => {
                if (!drag.hasUrls || drag.urls.length !== 1) {
                    drag.accepted = false;
                    return false;
                }

                const url = drag.urls[0];
                const shouldAccept = root.shouldAcceptUrl(url);
                if (!shouldAccept) {
                    drag.accepted = false;
                    return false;
                }

                urlLabel.text = `<font color="gray">Drop "<font color="text">${UrlUtils.name(url)}</font>"?</font>`;
            }
            onExited: {
                root.updateLabel();
            }
            onDropped: drop => {
                root.url = drop.urls[0];
                root.updateLabel();
            }
        }
    }

    Button {
        text: "Browse"
        onClicked: root.browseButtonClicked()
    }
}
