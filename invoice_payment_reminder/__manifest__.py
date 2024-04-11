{
    'name': 'Invoice Due Payment Reminder',
    'version': '17.0.1.0',
    'summary': 'Invoice due payment reminders for timely follow-up.',
    'description': 'The Payment Reminder module automates the process of sending payment reminders to customers or clients with outstanding invoices or pending payments.' 
                    'This helps businesses maintain healthy cash flow and minimize late payments.' 
                    'With customizable email templates and scheduling options, users can efficiently manage reminders,'
                    ' reducing manual effort and ensuring timely follow-up with customers.',
    'author': 'Abhilash Pathak',
    'maintainer': 'Abhilash Pathak',
    'depends': ['account'],
    'data': [
        'data/payment_reminder_cron.xml',
        'data/payment_reminder_email_template.xml',
    ],
}
