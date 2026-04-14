# AM Tech Website - Setup Guide

## Quick Start

Your website contact form is now fully functional! Follow these steps to get it working:

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Gmail (Required for Email Functionality)

#### Option A: Using Your Personal Gmail (Recommended)
1. Go to your Gmail account settings
2. Enable **2-Step Verification** (if not already enabled)
3. Create an **App Password**:
   - Visit: https://myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Google will generate a 16-character password
4. Open `.env` file and update:
   ```
   SENDER_EMAIL=amir2013.cr7@gmail.com
   SENDER_PASSWORD=xxxx xxxx xxxx xxxx
   ```

#### Option B: Using Alternative Email Services
Update `.env` with your provider's SMTP details:
- **Outlook**: smtp-mail.outlook.com:587
- **SendGrid**: smtp.sendgrid.net:587
- **Mailgun**: smtp.mailgun.org:587

### 3. Run the Server
```bash
python app.py
```

The server will start at `http://localhost:5000`

### 4. Test the Contact Form
- Open `http://localhost:5000` in your browser
- Fill out the contact form
- Submit and verify the email arrives at `amir2013.cr7@gmail.com`

---

## File Structure
```
am tech web/
├── code.html          ← Your website (updated with form JS)
├── DESIGN.md          ← Design system documentation
├── app.py             ← Python Flask backend
├── requirements.txt   ← Python dependencies
├── .env               ← Configuration (keep secure!)
└── README.md          ← This file
```

## Features Included
✓ Responsive contact form (design preserved)  
✓ Real-time form validation  
✓ Success/error messages with animations  
✓ Email notifications sent to amir2013.cr7@gmail.com  
✓ Loading state on submit button  
✓ CORS enabled for production deployment  

## Deployment Options

### Local Testing
```bash
python app.py
```

### Production Deployment (Heroku/Vercel/Railway)
1. Ensure all dependencies in `requirements.txt`
2. Set environment variables in your hosting platform
3. Update server address in contact form JavaScript if needed
4. Deploy Flask app and update HTML to point to new backend URL

### Simple Alternative: Using Formspree (No Backend Setup)
If you don't want to run Python, replace the form submission in `code.html` with:
```html
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

---

## Troubleshooting

**"Email not sending"**
- Verify SENDER_EMAIL and SENDER_PASSWORD in `.env`
- Check that 2FA is enabled on Gmail
- Confirm App Password is correct (no spaces in actual password)

**"Connection refused"**
- Make sure `python app.py` is running
- Check that port 5000 is not in use

**"CORS error"**
- Flask-CORS is already configured
- If deploying, ensure frontend URL is allowed

---

## Next Steps

1. ✅ Update `.env` with your email credentials
2. ✅ Run `python app.py`
3. ✅ Test the contact form on `http://localhost:5000`
4. ✅ Deploy when ready (preserve `.env` security)

Your website is ready to receive inquiries! 🚀
