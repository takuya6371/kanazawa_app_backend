import datetime

def checkDate(date:str):
    try:
        newDate=datetime.datetime.strptime(date,"%Y/%m/%d")
        return True
    except ValueError:
        return False

def get_today(format:str):
    return datetime.datetime.now().strftime(format)