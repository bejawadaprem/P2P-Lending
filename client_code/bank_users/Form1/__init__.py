from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("bank_users.Form1")

  def login_signup_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert("Logged out sucessfully")
    anvil.users.logout()
    open_form('bank_users.main_form')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_profile')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.new_loan_request')

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_loan_close')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_today_dues')

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.application_tracker')

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_foreclosure_request')

  def outlined_button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_discount_coupons')

  def outlined_button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_view_portfolio')

  def about_main_form_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('bank_users.borrower_rgistration_form.borrower_about')
