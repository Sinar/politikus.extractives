# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s politikus.extractives -t test_extractive_concession.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src politikus.extractives.testing.POLITIKUS_EXTRACTIVES_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/politikus/extractives/tests/robot/test_extractive_concession.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Extractive Concession
  Given a logged-in site administrator
    and an add Extractive Concession form
   When I type 'My Extractive Concession' into the title field
    and I submit the form
   Then a Extractive Concession with the title 'My Extractive Concession' has been created

Scenario: As a site administrator I can view a Extractive Concession
  Given a logged-in site administrator
    and a Extractive Concession 'My Extractive Concession'
   When I go to the Extractive Concession view
   Then I can see the Extractive Concession title 'My Extractive Concession'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Extractive Concession form
  Go To  ${PLONE_URL}/++add++Extractive Concession

a Extractive Concession 'My Extractive Concession'
  Create content  type=Extractive Concession  id=my-extractive_concession  title=My Extractive Concession

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Extractive Concession view
  Go To  ${PLONE_URL}/my-extractive_concession
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Extractive Concession with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Extractive Concession title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
