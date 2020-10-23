while(1):
    
    

    import smtplib
    import time

    from pytrends.request import TrendReq

    # Only need to run this once, the rest of requests will use the same session.
    pytrend = TrendReq()

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list=['tshirt'],timeframe='now 7-d',geo='US')


    # Related Queries, returns a dictionary of dataframes
    related_queries_dict = pytrend.related_queries()
    D=related_queries_dict['tshirt']['rising']


    gmail_user = 'yabous.xman@gmail.com'
    gmail_password = 'qbnrkjfgestijpwu'

    try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_password)
            msg=D
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            server.sendmail(gmail_user, gmail_user, message)
            server.quit()
            print(msg)
    except:
        print ('Something went wrong...')

    time.sleep( 30)

