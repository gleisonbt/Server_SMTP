"""
import smtplib
servidor_email = smtplib.SMTP('smtp.gmail.com', 587)

print(servidor_email.starttls())

servidor_email.login('brittobaptista93@gmail.com', 'rgor bgcv tjnr ykmt')

remetente = 'brittobaptista93@gmail.com'
destinatarios = ['gleison@cotemig.com.br', 'gleisoneinstein@hotmail.com.br']
conteudo = 'Ola este e um email de teste.'

servidor_email.sendmail(remetente, destinatarios, conteudo)

servidor_email.quit()
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    # Configurações do servidor SMTP
    servidor_smtp = 'smtp.gmail.com'
    porta = 587  # Porta padrão para SMTP
    usuario = 'brittobaptista93@gmail.com'
    senha = 'rgor bgcv tjnr ykmt'
    
    # Criando uma mensagem
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto
    
    # Adicionando corpo à mensagem
    msg.attach(MIMEText(mensagem, 'plain'))
    
    # Criando conexão com o servidor SMTP
    try:
        servidor = smtplib.SMTP(host=servidor_smtp, port=porta)
        servidor.starttls()  # Habilita criptografia TLS
        servidor.login(usuario, senha)
        
        # Enviando e-mail
        servidor.send_message(msg)
        print("E-mail enviado com sucesso para", destinatario)
        
    except Exception as e:
        print("Erro ao enviar e-mail:", str(e))
        
    finally:
        servidor.quit()

# Exemplo de uso
if __name__ == "__main__":
    destinatario = 'gleison@cotemig.com.br'
    assunto = 'Teste de e-mail'
    mensagem = 'Este é um e-mail de teste.'
    
    enviar_email(destinatario, assunto, mensagem)
