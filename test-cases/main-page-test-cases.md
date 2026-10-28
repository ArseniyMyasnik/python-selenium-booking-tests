# General Test Cases

## Test Case MP-1: Main Page Is Opened
**Preconditions:**
- The `open_main_page` fixture is configured and opens the main page by default.

**Steps:**
1. Run the test with the `open_main_page` fixture.
2. Verify that the main page is opened.

**Expected Result:**
- The browser is opened on the main page.

## Test Case MP-2: The "Book Now" Button Scrolls the Page to the "Our Rooms" Section
**Preconditions:**
- The main page is opened, and the top part of the page is visible without scrolling.

**Steps:**
1. Click the "Book Now" button.

**Expected Result:**
- The page scrolls to the "Our Rooms" section.

# Date Filter Test Cases

## Test Case MP-3.1: Check Date Availability With Valid Dates
**Preconditions:**
- The main page is scrolled to the "Check Availability & Book Your Stay" section.

**Steps:**
1. Enter Check In and Check Out dates, where the second date is later than the first.
2. Click Check Availability.

**Expected Result:**
- Available rooms appear in the Our Rooms section.

## Test Case MP-3.2: Check Date Availability When the Check-In Date Is Later Than the Check-Out Date
**Preconditions:**
- The main page is scrolled to the "Check Availability & Book Your Stay" section.

**Steps:**
1. Enter Check In and Check Out dates, where the second date is earlier than the first.
2. Click Check Availability.

**Expected Result:**
- An invalid date error appears.

## Test Case MP-3.3: Check Date Availability With Past Dates
**Preconditions:**
- The main page is scrolled to the "Check Availability & Book Your Stay" section.

**Steps:**
1. Enter past Check In and Check Out dates.
2. Click Check Availability.

**Expected Result:**
- An invalid date error appears.

# "Send Us a Message" Form Test Cases

## Test Case MP-4.1: Click "Submit" Without Filling Out the Form
**Preconditions:**
1. The "Send Us a Message" form is opened.

**Steps:**
1. Leave the form fields empty.
2. Click "Submit".

**Expected Result:**
- An error appears saying that the form fields must be filled in.

## Test Case MP-4.2: Name Field Tests
**Preconditions:**
1. The "Send Us a Message" form is opened.

**Steps:**
1. Enter names in the Name field.
2. Click "Submit".

**Test Data and Expected Result:**
|No.|Name|Expected Result|
|-|---|---------------|
|1|Ivan|The name is accepted, and no invalid name error appears.|
|2|John|The name is accepted, and no invalid name error appears.|
|3|Ivan!|The name is accepted, and no invalid name error appears.|
|4|Ivan1|The name is accepted, and no invalid name error appears.|

## Test Case MP-4.3: Email Field Tests
**Preconditions:**
1. The "Send Us a Message" form is opened.

**Steps:**
1. Enter email values in the Email field.
2. Click "Submit".

**Test Data and Expected Result:**
|No.|Email|Expected Result|
|-|-----|---------------|
|1|arseniy|The entered value is not an email address, and an invalid email error appears.|
|2|arseniym148@gmail|The email is accepted, and no invalid email error appears.|
|3|arseniym148\@gmail.com|The email is accepted, and no invalid email error appears.|

## Test Case MP-4.4: Phone Field Tests
**Preconditions:**
1. The "Send Us a Message" form is opened.

**Steps:**
1. Enter phone numbers in the Phone field.
2. Click "Submit".

**Test Data and Expected Result:**
|No.|Phone Number|Expected Result|
|-|------------|---------------|
|1|aaaaa|The phone number is rejected because it is shorter than 11 characters, and a length error appears.|
|2|0123456789|The phone number is rejected because it is shorter than 11 characters, and a length error appears.|
|3|+0123456789|The phone number is accepted, and no length error appears.|
|4|012 345 67 89|The phone number is accepted, and no length error appears.|
|5|012 345-67-89|The phone number is accepted, and no length error appears.|
|6|(012) 345-67-89|The phone number is accepted, and no length error appears.|
|7|01234567890|The phone number is accepted, and no length error appears.|
|8|0*21|The phone number is accepted, and no length error appears.|
|9|0*22|The phone number is rejected because it is longer than 21 characters, and a length error appears.|

## Test Case MP-4.5: Subject Field Tests
**Preconditions:**
1. The "Send Us a Message" form is opened.

**Steps:**
1. Enter subjects in the Subject field.
2. Click "Submit".

**Test Data and Expected Result:**
|No.|Subject|Expected Result|
|-|-------|---------------|
|1|abcd|The minimum subject length is 5 characters, and an invalid subject error appears.|
|2|abcde|The subject is accepted, and no invalid subject error appears.|
|3|a*100|The subject is accepted, and no invalid subject error appears.|
|4|a*101|The maximum subject length is 100 characters, and an invalid subject error appears.|

## Test Case MP-4.6: Message Field Tests
**Preconditions:**
1. The "Send Us a Message" form is opened.

**Steps:**
1. Enter messages in the Message field.
2. Click "Submit".

**Test Data and Expected Result:**
|No.|Message|Expected Result|
|-|-------|---------------|
|1|a*19|The minimum message length is 20 characters, and an invalid message error appears.|
|2|a*20|The message is accepted, and no invalid message error appears.|
|3|a*2000|The message is accepted, and no invalid message error appears.|
|4|a*2001|The maximum message length is 2000 characters, and an invalid message error appears.|

## Test Case MP-4.7: All Fields Are Filled Correctly
**Preconditions:**
1. The "Send Us a Message" form is opened.

**Steps:**
1. Enter `Name` in the Name field.
2. Enter `arseniym148\@gmail.com` in the Email field.
3. Enter `+1234567890` in the Phone field.
4. Enter `Subject` in the Subject field.
5. Enter `MessageMessageMessageMessage` in the Message field.
6. Click "Submit".

**Expected Result:**
1. A successful message submission notification appears.
2. The notification contains the correct name and subject.
