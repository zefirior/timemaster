UI_PATH=../ui
WIDG_PATH=../src/widgets

pyuic5 ${UI_PATH}/continue_dialog.ui -o     ${WIDG_PATH}/continue_setuper.py
pyuic5 ${UI_PATH}/edit_interval.ui -o       ${WIDG_PATH}/recipe_edit_setuper.py
pyuic5 ${UI_PATH}/finish_dialog.ui -o       ${WIDG_PATH}/finish_setuper.py
pyuic5 ${UI_PATH}/interval.ui -o            ${WIDG_PATH}/main_setuper.py
pyuic5 ${UI_PATH}/tomate_view.ui -o         ${WIDG_PATH}/tomate_edit_setuper.py
pyuic5 ${UI_PATH}/tomate_container.ui -o    ${WIDG_PATH}/tomate_view_setuper.py
