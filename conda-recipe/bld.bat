xcopy /e "%RECIPE_DIR%"\.. "%SRC_DIR%"
"%PYTHON%" setup.py install
xcopy /e "%SRC_DIR%\sql_novice_survey\*.*" "%SP_DIR%\sql_novice_survey"
if errorlevel 1 exit 1