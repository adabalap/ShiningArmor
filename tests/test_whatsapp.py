import logging
from ShiningArmor import whatsapp


logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.INFO)

if __name__ == "__main__":

    wa = whatsapp.init(display=False)
    # wa['contact'] = 'Phani Adabala'
    wa['contact'] = 'SputnikBot'
    wa['xpath'] = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
    wa['message'] = 'Hello from ... Sputnik BOT\n- test message'

    wa = whatsapp.locate_contact(wa)

    if wa["rc"] == 0:
        wa = whatsapp.locate_message_box(wa)

    if wa["rc"] == 0:
        wa = whatsapp.send_message(wa)

    if wa["rc"] == 0:
        wa = whatsapp.close(wa, display=False)

    if wa["rc"] == 0:
        logging.info(f'WhatsApp Message sent SUCCESSFULLY!')
