from gmail import GMail, Message

def sent_mail(x):
    gmail = GMail("dangsonhai26061995@gmail.com","Theeternal0610")
    html_content = """Yêu cầu của bạn đã được xử lý, 
    chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. 
    Cảm ơn bạn đã sử dụng dịch vụ của 'Mùa Đông Không Lạnh'"""
    msg = Message('Mùa Đông Không Lạnh',to = x ,html = html_content)
    gmail.send(msg)