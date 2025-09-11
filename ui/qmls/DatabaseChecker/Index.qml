import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

import internal.ui.vm 1.0
import "../Components"

Page {
    id: root

    property bool showConfirmConnectionDialog: false

    signal ready

    function confirm(source: string): void {
        if (!source)
            throw new Error("source is required");

        const shouldConfirm = (source === 'continueButton' && vm.canConfirmSilently) || source === 'dialog';

        if (shouldConfirm) {
            vm.confirmCurrentConnection();
            root.ready();
        } else {
            root.showConfirmConnectionDialog = true;
        }
    }

    DatabaseInitViewModel {
        id: vm

        onSelectFileUrlChanged: {
            selectOrCreate.selectFileUrl = this.selectFileUrl;
        }
        onDirectoryUrlChanged: {
            selectOrCreate.directoryUrl = this.directoryUrl;
        }
        onFilenameChanged: {
            selectOrCreate.filename = this.filename;
        }
        onDatabaseUrlChanged: {
            confirmConnectionDialog.databaseUrl = this.databaseUrl;
        }
        onDatabaseInfoChanged: {
            databaseInfo.info = this.databaseInfo;
        }
        onCanContinueChanged: {
            continueButton.enabled = this.canContinue;
        }
    }

    Page {
        padding: 10
        anchors.fill: parent

        Dialog_ConfirmConnection {
            id: confirmConnectionDialog

            anchors.centerIn: parent
            visible: root.showConfirmConnectionDialog

            onAccepted: root.confirm('dialog')
            onClosed: root.showConfirmConnectionDialog = false

            databaseUrl: vm.databaseUrl
        }

        ColumnLayout {
            width: parent.width
            spacing: 2

            SectionTitle {
                text: qsTr('Select or Create Database')
            }

            Section_SelectOrCreate {
                id: selectOrCreate
                selectFileUrl: vm.selectFileUrl
                createDirectoryUrl: vm.directoryUrl
                createFilename: vm.filename

                onUiModeChanged: uiMode => vm.uiMode = uiMode
                onSelectFileUrlChanged: {
                    vm.selectFileUrl = selectFileUrl;
                }
                onCreateDirectoryUrlChanged: {
                    vm.directoryUrl = createDirectoryUrl;
                }
                onCreateFilenameChanged: {
                    vm.filename = createFilename;
                }
                onConfirmCreate: {
                    vm.loadDatabaseInfo();
                }
            }

            HorizontalDivider {}

            SectionTitle {
                text: 'Database Status'
            }

            Section_DatabaseInfo {
                id: databaseInfo
                info: vm.databaseInfo
            }
        }

        footer: Pane {
            padding: 5
            RowLayout {
                Button {
                    id: continueButton
                    Layout.alignment: Qt.AlignHCenter

                    text: qsTr('Continue')
                    enabled: vm.canContinue

                    onClicked: root.confirm('continueButton')
                }
            }
        }
    }
}
