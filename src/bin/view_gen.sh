UI_PATH=../ui

pyuic5 ${UI_PATH}/continue_dialog.ui -o ${UI_PATH}/continue_dialog.py
pyuic5 ${UI_PATH}/edit_interval.ui -o ${UI_PATH}/edit_interval.py
pyuic5 ${UI_PATH}/finish_dialog.ui -o ${UI_PATH}/finish_dialog.py
pyuic5 ${UI_PATH}/interval.ui -o ${UI_PATH}/interval_view.py
pyuic5 ${UI_PATH}/tomate_view.ui -o ${UI_PATH}/tomate_view.py
