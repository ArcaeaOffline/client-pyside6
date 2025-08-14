import QtQuick
import QtQuick.Dialogs

import internal.ui.utils

SelectorBase {
    id: base

    FileDialog {
        id: fileDialog
        onAccepted: {
            base.url = this.selectedFile;
        }
    }

    function isFileUrlValid(url: url): bool {
        return url.toString().startsWith("file://");
    }

    property alias fileUrl: base.url
    onFileUrlChanged: {
        if (isFileUrlValid(fileUrl)) {
            fileDialog.selectedFile = fileUrl;
            fileDialog.currentFolder = UrlUtils.parent(fileUrl);
        }
    }

    shouldAcceptUrl: url => UrlUtils.isFile(url)
    onBrowseButtonClicked: {
        fileDialog.open();
    }
    placeholderText: '<font color="gray">Select a file…</font>'
}
