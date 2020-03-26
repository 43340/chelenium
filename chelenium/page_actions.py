from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def click(element):
    print(f"DEBUG | {element._name}.click()")
    element.click()


def send_text(element, text):
    print(f"DEBUG | {element._name}.send_text({text})")
    element.send_keys(text)


def update_text(element, text):
    print(f"DEBUG | {element._name}.update_text({text})")
    element.clear()
    element.send_keys(text)

def hover(driver, element):
    print(f"DEBUG | {element._name}.hover()")
    ActionChains(driver).move_to_element(element).perform()


def select(element, by, value):
    sel = Select(element)

    if by == "text":
        print(f"DEBUG | {element._name}.select_by_visible_text({value})")
        sel.select_by_visible_text(value)
    elif by == "value":
        print(f"DEBUG | {element._name}.select_by_value({value})")
        sel.select_by_value(value)
    else:
        print(f"DEBUG | {element._name}.select_by_index({value})")
        sel.select_by_index(value)
