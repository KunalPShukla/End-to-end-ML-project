import sys

def error_message_detail(error,error_detail:sys):
    exc_key,exc_value,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno
    main_error=str(error)
    error_message=f"Error occured in file: {file_name}\nLine number:{line_no}, error_message:{main_error}"
    # print(error_message)
    return error_message

class CustomException(Exception):
    def __init__(self,error,error_detail:sys):
        super().__init__(str(error))
        self.error_message=error_message_detail(error,error_detail)
        
    def __str__(self):    
        return self.error_message