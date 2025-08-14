import QtQuick
import QtQuick.Dialogs

import internal.ui.utils

SelectorBase {
    id: base

    FolderDialog {
        id: folderDialog
        selectedFolder: base.directoryUrl
        onAccepted: {
            base.directoryUrl = this.selectedFolder;
            this.currentFolder = this.selectedFolder;
        }
    }

    property alias directoryUrl: base.url

    shouldAcceptUrl: url => UrlUtils.isDir(url)
    onBrowseButtonClicked: {
        folderDialog.open();
    }
    placeholderText: '<font color="gray">Select a directory…</font>'
}
