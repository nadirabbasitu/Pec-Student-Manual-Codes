for %%x in (*.docx) do (
    echo %%~nx
   officetopdf.exe "%%x" "%%~nx".pdf
   del "%%x"
   
)
pause >nul

