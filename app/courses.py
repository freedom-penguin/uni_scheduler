USERNAME = "admin"
PASSWORD = "password"
IP = "localhost"
PORT = 27017

"""

      _id: -> Εξάμηνο / Semester
      str : list[str] -> Μάθημα - Course  /  Ώρες διδαδασκαλίας - Teaching Hours 
    
      names of professors will not be added.
"""

SEMESTERS = [
   
    {
        "_id": "1",
        "lessons": [
            "Μαθηματική Ανάλυση I",
            "Γραμμική Άλγεβρα",
            "Εισαγωγή στην Επιστήμη των Υπολογιστών",
            "Προγραμματισμός Υπολογιστών",
            "Διακριτά Μαθηματικά",
            "Φυσική"            
        ]
        
    },
    
            
    {
        "_id": "2",
        "lessons": [
            "Σχεδίαση και Ανάλυση Αλγορίθμων",
            "Πιθανότητες και Στατιστική",
            "Μαθηματική Ανάλυση ΙΙ",
            "Αντικειμενοστρεφής Προγραμματισμός",
            "Ψηφιακή Σχεδίαση",
            "Θεωρία Κυκλωμάτων"
        ]
    },
    
    {
        "_id": "3",
         
        "lessons": [
            "Αλγόριθμοι και Πολυπλοκότητα",
            "Ηλεκτρονική",
            "Δομές Δεδομένων",
            "Δίκτυα Υπολογιστών Ι",
            "Λειτουργικά Συστήματα Ι",
            "Αρχιτεκτονική Υπολογιστών"
        ]
    },
    
    {
        "_id": "4",
        "lessons": [
            "Βάσεις Δεδομένων Ι",
            "Δίκτυα Υπολογιστών ΙΙ",
            "Λειτουργικά Συστήματα ΙΙ",
            "Μεθοδολογίες Ανάπτυξης Εφαρμογών",
            "Σχεδίαση Ψηφιακών Συστημάτων",
            "Σήματα και Συστήματα",
            "Σύνταξη Τεχνικών Κειμένων"
        ]
    },
    
    {
        "_id": "5",
        "lessons": [
            "Βάσεις Δεδομένων ΙΙ",
            "Δικτυακός Προγραμματισμός",
            "Ανάλυση και Σχεδιασμός Πληροφοριακών Συστημάτων",
            "Τεχνητή Νοημοσύνη",
            "Ψηφιακή Επεξεργασία Σήματος",
            "Εισαγωγή στον Παράλληλο Υπολογισμό"
        ]
    },
    
    {
        "_id": "6",
        "lessons": [
            "Τεχνολογία Λογισμικού",
            "Ασφάλεια στην Τεχνολογία της Πληροφορίας",
            "Μεταγλωττιστές",
            "Μικροηλεκτρονική",
            "Κατανεμημένα Συστήματα",
            "Ψηφιακές Επικοινωνίες"
        ]
    }
]


PROGRAM = {

    "9-10": {
        "Monday": [
            "Σχεδίαση και Ανάλυση Αλγορίθμων (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ],
        
        "Tuesday": [
            "Ψηφιακή Σχεδίαση (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113)"
            ],
        
        "Wednesday": [
            "Πιθανότητες και Στατιστική (2ο Εξάμηνο, 2ο Τμήμα, Κ16.114)"
            ],
        
        "Thursday": [
            ],
        
        "Friday": [
            "Σχεδίαση και Ανάλυση Αλγορίθμων (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ]
    },
    
    "10-11": {
        "Monday": [
            "Σχεδίαση και Ανάλυση Αλγορίθμων (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ],
        
        "Tuesday": [
            "Ψηφιακή Σχεδίαση (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113)"
            ],
        
        "Wednesday": [
            "Πιθανότητες και Στατιστική (2ο Εξάμηνο, 2ο Τμήμα, Κ16.114)"
            ],
        
        "Thursday": [
            "Σχεδίαση και Ανάλυση Αλγορίθμων (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113)"
            ],
        
        "Friday": [
            "Σχεδίαση και Ανάλυση Αλγορίθμων (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ],
    },
    
    "11-12": {
        "Monday": [],
        
        "Tuesday": [
            "Ψηφιακή Σχεδίαση (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113)"
            ],
        
        "Wednesay": [],
        
        "Thursday": [
            "Σχεδίαση και Ανάλυση Αλγορίθμων (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113)"
            ],
        
        "Friday": [
            "Πιθανότητες και Στατιστική (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ],
    },
    
    "12-13": {
        "Monday": [
            "Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ],
        "Tuesday": [
            "Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113 ή Κ16.114)"
            ],
        
        "Wednesday": [
            "Πιθανότητες και Στατιστική (2ο Εξάμηνο, 2ο Τμήμα, Κ16.114)"
            ],
        
        "Thursday": [
            "Μαθηματική Ανάλυση ΙΙ (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"
                  ],
        
        "Friday": [
            "Πιθανότητες και Στατιστική (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ],
    },
    
    "13-14": {
        "Monday": [
            "Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ],
        
        "Tuesday": [
            "Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113 ή Κ16.114)"
            ],
        
        "Wednesday": [
            "Πιθανότητες και Στατιστική (2ο Εξάμηνο, 2ο Τμήμα, Κ16.114)"
            ],
        
        "Thursday": [
            "Μαθηματική Ανάλυση ΙΙ (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"
            ],
        
        "Friday": [
            "Μαθηματική Ανάλυση ΙΙ (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"
            ],
    },
    
    "14-15": {
        "Monday": ["Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Tuesday": ["Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113 ή Κ16.114)"],
        "Wednesday": ["Σχεδίαση και Ανάλυση Αλγορίθμων (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113)"],
        "Thursday": ["Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Friday": ["Μαθηματική Ανάλυση ΙΙ (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"],
    },
    
    "15-16": {
        "Monday": ["Θεωρία Κυκλωμάτων (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Tuesday": ["Ψηφιακή Σχεδίαση (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)", "Μαθηματική Ανάλυση ΙΙ (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"],
        "Wednesday": ["Μαθηματική Ανάλυση ΙΙ", "Σχεδίαση και Ανάλυση Αλγορίθμων (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113)"],
        "Thursday": ["Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Friday": [],
    },
    
    "16-17": {
        "Monday": ["Θεωρία Κυκλωμάτων (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Tuesday": ["Ψηφιακή Σχεδίαση (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)", "Μαθηματική Ανάλυση ΙΙ (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"],
        "Wednesday": ["Μαθηματική Ανάλυση ΙΙ (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Thursday": ["Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Friday": [],
    },
    
    "17-18": {
        "Monday": ["Θεωρία Κυκλωμάτων (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Tuesday": ["Ψηφιακή Σχεδίαση (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Wednesday": ["Πιθανότητες και Στατιστική (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Thursday": ["Αντικειμενοστρεφής Προγραμματισμός (2ο Εξάμηνο, 2ο Τμήμα, Κ16.113)"],
        "Friday": [],
    },
    
    "18-19": {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": ["Πιθανότητες και Στατιστική (2ο Εξάμηνο, 1ο Τμήμα, Αμφιθέατρο)"],
        "Thursday": ["Θεωρία Κυκλωμάτων (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"],
        "Friday": [],
    },
    
    "19-20": {
        "Monday": ["Θεωρία Κυκλωμάτων (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": ["Θεωρία Κυκλωμάτων (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"],
        "Friday": [],
    },
    
    "20-21": {
        "Monday": ["Θεωρία Κυκλωμάτων (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": ["Θεωρία Κυκλωμάτων (2ο Εξάμηνο, 2ο Τμήμα, Αμφιθέατρο)"],
        "Friday": [],
    }
}