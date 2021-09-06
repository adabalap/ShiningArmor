import logging
from ShiningArmor import whatsapp


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

if __name__ == "__main__":

    wa = whatsapp.init()
    wa['contact'] = 'Phani Adabala'
    wa['message'] = 'Hello from ... Sputnik BOT'

    wa = whatsapp.locate_contact(wa)

    if wa["rc"] == 0:
        wa = whatsapp.locate_message_box(wa)

    if wa["rc"] == 0:
        wa = whatsapp.send_message(wa)

    if wa["rc"] == 0:
        wa = whatsapp.close(wa)

    if wa["rc"] == 0:
        logging.info(f'WhatsApp Message sent SUCCESSFULLY!')
