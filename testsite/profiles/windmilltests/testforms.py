# -*- coding: utf-8 -*-

from windmill.authoring import WindmillTestClient


def test_ajax_forms():
    client = WindmillTestClient(__name__)
    client.click(link=u'Edit')
    client.waits.forPageLoad(timeout=u'20000')
    client.waits.forElement(link=u'Login', timeout=u'8000')
    client.click(link=u'Login')
    client.click(id=u'id_username')
    client.type(text=u'admin', id=u'id_username')
    client.type(text=u'admin', id=u'id_password')
    client.click(value=u'login')
    client.waits.forPageLoad(timeout=u'20000')

    client.waits.forElement(timeout=u'8000', id=u'id_birth')
    client.click(id=u'id_birth')
    client.waits.sleep(milliseconds=1000)
    client.waits.forElement(
        xpath=u"//div[@id='ui-datepicker-div']/div/div/select[2]",
        id=u'id_birth')
    client.select(classname=u'ui-datepicker-month', val=u'10')
    client.select(classname=u'ui-datepicker-year', val=u'1986')
    client.click(link=u'10')
    client.click(name=u'save')

    #And this should work anyway:
    client.asserts.assertText(id="message", validator="Done. Reloading...")
    client.waits.forPageLoad(timeout=u'20000')

    client.click(timeout=u'8000', id=u'id_birth')
    client.type(text=u'1987-12-1122', id=u'id_birth')
    client.click(name=u'save')
    client.waits.forElement(id="birth_error")
    client.asserts.assertText(id="birth_error",
                              validator="Enter a valid date.")
