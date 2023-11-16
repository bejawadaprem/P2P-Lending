from ._anvil_designer import star_1_borrower_registration_form_begin_8Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class star_1_borrower_registration_form_begin_8(star_1_borrower_registration_form_begin_8Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    account_name = self.text_box_1.text
    account_type = self.text_box_2.text
    account_number = self.text_box_3.text
    bank_branch = self.text_box_4.text
    user_id = self.userId
    if not account_name or not account_type or not account_number or not bank_branch:
      Notification("please fill the all required fields").show()
    else:
      anvil.server.call('add_lendor_bank_details_form_1', account_name, account_type,account_number,bank_branch, user_id)
      open_form('lendor_registration_form.Lender_reg_bankdirect_bank_form_2',user_id=self.userId)

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_form_6',user_id=self.userId)

  def button_3_click(self, **event_args):
    open_form("bank_users.user_form")
