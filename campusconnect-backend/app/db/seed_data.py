"""
Seed dataset containing all initial data matching the Figma UI and specifications.
"""

EVENTS_SEED = [
    {
        "id": "1",
        "slug": "ai-and-the-future",
        "title": "AI & the Future",
        "tag": "TECH TALK",
        "category": "Tech",
        "interests": ["AI & ML", "Web Dev"],
        "hero_badge": "TECH TALK",
        "date": "12 Nov 2026",
        "day": "Thu",
        "time": "10:00 AM - 12:00 PM",
        "location": "Main Auditorium Hall A",
        "organizer": "AI Club (Tech Club)",
        "organizer_id": "tech-club",
        "price": "Free Entry",
        "price_val": 0.0,
        "is_featured": True,
        "badge_color": "blue",
        "icon": "cpu",
        "short_desc": "A practical inspiring talk with founders and engineers building real AI.",
        "description": "Discover how large language models, agentic workflows, and multimodal systems are reshaping product development. Join leading researchers and student builders as they demo autonomous systems and discuss career pathways in modern AI engineering.",
        "perks": [
            "Networking session pass with AI founders",
            "Hands-on code demo repository & sample files",
            "Official certificate of participation",
            "Live Q&A and hardware demo showcase"
        ],
        "speakers": [
            {"name": "Dr. Aris Thorne", "role": "Principal AI Researcher", "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150"},
            {"name": "Siddharth Rao", "role": "Lead Architect at Agentic Labs", "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150"}
        ],
        "registered_count": 142,
        "capacity": 200,
        "status": "Active"
    },
    {
        "id": "2",
        "slug": "aura-cultural-fest",
        "title": "Aura Cultural Fest",
        "tag": "CULTURE",
        "category": "Culture",
        "interests": ["Design", "Leadership"],
        "hero_badge": "CULTURAL GALA",
        "date": "19 Nov 2026",
        "day": "Fri",
        "time": "4:00 PM - 10:00 PM",
        "location": "Campus Amphitheatre",
        "organizer": "Cultural Arts Council",
        "organizer_id": "arts-council",
        "price": "Free Entry",
        "price_val": 0.0,
        "is_featured": True,
        "badge_color": "rose",
        "icon": "sparkles",
        "short_desc": "Annual inter-college cultural gala featuring live musical bands & art showcases.",
        "description": "Experience an electric evening celebrating youth culture, performing arts, acoustic indie bands, and student dance showcases. Grab food truck specials and participate in campus-wide open-mic spotlights.",
        "perks": [
            "Festival wristband & glow accessories",
            "Front-stage access voucher",
            "Campus food stall discount vouchers",
            "Entry to evening celebrity performance"
        ],
        "speakers": [
            {"name": "Maya Sen", "role": "Head Curator, Campus Arts", "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150"}
        ],
        "registered_count": 310,
        "capacity": 500,
        "status": "Active"
    },
    {
        "id": "3",
        "slug": "codesphere-hackathon",
        "title": "CodeSphere Hackathon",
        "tag": "HACKATHON",
        "category": "Tech",
        "interests": ["AI & ML", "Web Dev", "Leadership"],
        "hero_badge": "24H HACKATHON",
        "date": "26 Nov 2026",
        "day": "Sat",
        "time": "9:00 AM - 9:00 PM",
        "location": "CS Innovation Lab & Maker Space",
        "organizer": "Developer Student Guild (Tech Club)",
        "organizer_id": "tech-club",
        "price": "Free Entry",
        "price_val": 0.0,
        "is_featured": True,
        "badge_color": "violet",
        "icon": "code-2",
        "short_desc": "Build something incredible in 24 hours with AI, web, and mobile tech.",
        "description": "Assemble your team or match with fellow builders on campus. Tackle industry problem statements across healthcare, education, sustainability, and generative tools. $10,000+ in sponsor prize pools, API credits, and venture mentor evaluations.",
        "perks": [
            "Exclusive CodeSphere participant kit & swag hoodie",
            "Complimentary meals, energy snacks & midnight pizza",
            "Cloud hosting credits & API access tokens",
            "1-on-1 mentorship with senior engineering leads"
        ],
        "speakers": [
            {"name": "Devin Chen", "role": "Founding Engineer @ VectorDB", "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150"}
        ],
        "registered_count": 210,
        "capacity": 250,
        "status": "Active"
    },
    {
        "id": "4",
        "slug": "frontend-sprint",
        "title": "Frontend Sprint: Web UI Masterclass",
        "tag": "WORKSHOP",
        "category": "Workshops",
        "interests": ["Web Dev", "Design"],
        "hero_badge": "HANDS-ON WORKSHOP",
        "date": "02 Dec 2026",
        "day": "Wed",
        "time": "2:00 PM - 5:00 PM",
        "location": "Computer Lab 3 (West Wing)",
        "organizer": "Web Dev Society",
        "organizer_id": "web-society",
        "price": "Free Entry",
        "price_val": 0.0,
        "is_featured": False,
        "badge_color": "blue",
        "icon": "layout",
        "short_desc": "Level up modern web architecture, CSS animations, and design system engineering.",
        "description": "Learn how modern frontend engineering bridges Figma design tokens with high-performance components. We'll build real reactive micro-interactions, responsive grids, and accessible components.",
        "perks": [
            "Starter repo & design system component kit",
            "Lab workstation access",
            "Peer code review session"
        ],
        "speakers": [
            {"name": "Priya Sharma", "role": "Senior UI Engineer", "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=150"}
        ],
        "registered_count": 78,
        "capacity": 90,
        "status": "Active"
    },
    {
        "id": "5",
        "slug": "design-jam-for-good",
        "title": "Design Jam: UI/UX for Good",
        "tag": "DESIGN",
        "category": "Career",
        "interests": ["Design", "Leadership"],
        "hero_badge": "CREATIVE SPRINT",
        "date": "05 Dec 2026",
        "day": "Sat",
        "time": "11:00 AM - 4:00 PM",
        "location": "Design Studio B, Faculty of Arts",
        "organizer": "Design Collective",
        "organizer_id": "design-collective",
        "price": "Free Entry",
        "price_val": 0.0,
        "is_featured": False,
        "badge_color": "amber",
        "icon": "pen-tool",
        "short_desc": "Design intuitive user flows and prototypes tackling social impact challenges.",
        "description": "A collaborative design sprint pairing designers and product strategists to redesign civic tech services, environmental tracking, and accessible campus tools.",
        "perks": [
            "Figma community template pack",
            "Design critique with industry designers",
            "Portfolio showcase opportunity"
        ],
        "speakers": [
            {"name": "Kavita Nair", "role": "Staff Product Designer", "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=150"}
        ],
        "registered_count": 64,
        "capacity": 80,
        "status": "Active"
    },
    {
        "id": "6",
        "slug": "deep-learning-workshop",
        "title": "Deep Learning & PyTorch Primer",
        "tag": "WORKSHOP",
        "category": "Workshops",
        "interests": ["AI & ML"],
        "hero_badge": "HANDS-ON LAB",
        "date": "15 Dec 2026",
        "day": "Tue",
        "time": "1:00 PM - 4:30 PM",
        "location": "Seminar Hall 2 & Cloud GPU Lab",
        "organizer": "AI Club (Tech Club)",
        "organizer_id": "tech-club",
        "price": "Free Entry",
        "price_val": 0.0,
        "is_featured": False,
        "badge_color": "indigo",
        "icon": "cpu",
        "short_desc": "From linear models to neural networks with live GPU execution.",
        "description": "Deep-dive into tensor operations, backpropagation, and training your first convolutional and transformer architectures using PyTorch and Colab Pro GPU clusters.",
        "perks": [
            "GPU compute credits",
            "Jupyter notebooks and starter code",
            "Certificate of completion"
        ],
        "speakers": [
            {"name": "Prof. N. K. Raman", "role": "Professor of Machine Learning", "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150"}
        ],
        "registered_count": 50,
        "capacity": 60,
        "status": "Active"
    }
]

USERS_SEED = [
    {
        "id": "usr-1",
        "email": "anwitha@campus.edu",
        "name": "Anwitha Guntupalli",
        "phone": "+91 98765 43210",
        "department": "Computer Science & Technology",
        "grade": "3rd Year CS",
        "student_id": "STU-2024-CS-094",
        "account_type": "Student Account",
        "role": "student",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=150",
        "interests": ["AI & ML", "Web Dev", "Design", "Leadership"]
    },
    {
        "id": "usr-org-1",
        "email": "lead@techclub.campus.edu",
        "name": "Tech Club Administrator",
        "phone": "+91 98999 11111",
        "department": "Faculty of Computer Engineering",
        "grade": "Faculty Coordinator",
        "student_id": "FAC-TC-001",
        "account_type": "Organizer Account",
        "role": "organizer",
        "organizer_id": "tech-club",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150",
        "interests": ["Tech", "Leadership"]
    }
]

REGISTRATIONS_SEED = [
    {
        "id": "reg-1",
        "event_id": "1",
        "user_id": "usr-1",
        "user_email": "anwitha@campus.edu",
        "user_name": "Anwitha Guntupalli",
        "phone": "+91 98765 43210",
        "department": "Computer Science & Technology",
        "registration_type": "Student Attendee",
        "ticket_id": "CC-2026-FUT-0481",
        "status": "CONFIRMED"
    },
    {
        "id": "reg-2",
        "event_id": "2",
        "user_id": "usr-1",
        "user_email": "anwitha@campus.edu",
        "user_name": "Anwitha Guntupalli",
        "phone": "+91 98765 43210",
        "department": "Computer Science & Technology",
        "registration_type": "General Access",
        "ticket_id": "CC-2026-AUR-1092",
        "status": "CONFIRMED"
    },
    {
        "id": "reg-3",
        "event_id": "3",
        "user_id": "usr-1",
        "user_email": "anwitha@campus.edu",
        "user_name": "Anwitha Guntupalli",
        "phone": "+91 98765 43210",
        "department": "Computer Science & Technology",
        "registration_type": "Hackathon Participant",
        "ticket_id": "CC-2026-CSH-3380",
        "status": "CONFIRMED"
    },
    # Additional attendees for Organizer attendee lists
    {
        "id": "reg-4",
        "event_id": "1",
        "user_id": None,
        "user_email": "riya.sharma@campus.edu",
        "user_name": "Riya Sharma",
        "phone": "+91 98111 22334",
        "department": "Information Science",
        "registration_type": "Student Attendee",
        "ticket_id": "CC-2026-FUT-0482",
        "status": "CONFIRMED"
    },
    {
        "id": "reg-5",
        "event_id": "1",
        "user_id": None,
        "user_email": "aman.kumar@campus.edu",
        "user_name": "Aman Kumar",
        "phone": "+91 98222 33445",
        "department": "Computer Science & Technology",
        "registration_type": "Student Attendee",
        "ticket_id": "CC-2026-FUT-0483",
        "status": "CONFIRMED"
    },
    {
        "id": "reg-6",
        "event_id": "1",
        "user_id": None,
        "user_email": "meera.patel@campus.edu",
        "user_name": "Meera Patel",
        "phone": "+91 98333 44556",
        "department": "Design & Media",
        "registration_type": "Student Attendee",
        "ticket_id": "CC-2026-FUT-0484",
        "status": "CONFIRMED"
    },
    {
        "id": "reg-7",
        "event_id": "1",
        "user_id": None,
        "user_email": "rohit.verma@campus.edu",
        "user_name": "Rohit Verma",
        "phone": "+91 98444 55667",
        "department": "Electronics & Comm",
        "registration_type": "Student Attendee",
        "ticket_id": "CC-2026-FUT-0485",
        "status": "CHECKED_IN"
    }
]

COBUILDERS_SEED = [
    {
        "id": "cb-1",
        "name": "Riya Sharma",
        "role": "Frontend Developer",
        "skills": ["React", "Tailwind", "TypeScript", "Next.js"],
        "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120",
        "match_score": "96%",
        "status": "Available",
        "bio": "Passionate about high-performance design systems and animations."
    },
    {
        "id": "cb-2",
        "name": "Aman Kumar",
        "role": "Backend & Systems Engineer",
        "skills": ["Python", "FastAPI", "PostgreSQL", "Docker"],
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120",
        "match_score": "92%",
        "status": "Looking for AI/Web squad",
        "bio": "Building scalable microservices and distributed event systems."
    },
    {
        "id": "cb-3",
        "name": "Meera Patel",
        "role": "UI/UX & Product Designer",
        "skills": ["Figma", "Wireframing", "User Research", "Design Systems"],
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120",
        "match_score": "88%",
        "status": "Open to Hackathons",
        "bio": "Product thinker crafting human-centered digital experiences."
    },
    {
        "id": "cb-4",
        "name": "Devin Chen",
        "role": "ML & Data Engineer",
        "skills": ["PyTorch", "Vector DBs", "LLMs", "LangChain"],
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120",
        "match_score": "85%",
        "status": "Available",
        "bio": "Interested in autonomous agents and embeddings for domain search."
    }
]

NOTIFICATIONS_SEED = [
    {
        "id": "notif-1",
        "user_id": "usr-1",
        "title": "Registration confirmed",
        "subtitle": "AI & the Future Tech Talk",
        "message": "You're registered for AI & the Future Tech Talk! Please arrive 15 minutes before session commencement with your digital event pass for priority scan-in.",
        "category": "Registration",
        "event_id": "1",
        "date": "Thursday, 12 Nov 2026",
        "time_slot": "10:00 AM - 12:00 PM",
        "venue": "Main Auditorium Hall A",
        "unread": True
    },
    {
        "id": "notif-2",
        "user_id": "usr-1",
        "title": "Event reminder",
        "subtitle": "Aura Cultural Fest Gala",
        "message": "Aura Cultural Fest schedule has been published! Musical band lineup begins at 6 PM. Check-in wristbands available from 3:30 PM at the main gates.",
        "category": "Reminder",
        "event_id": "2",
        "date": "Friday, 19 Nov 2026",
        "time_slot": "4:00 PM - 10:00 PM",
        "venue": "Campus Amphitheatre",
        "unread": False
    },
    {
        "id": "notif-3",
        "user_id": "usr-1",
        "title": "Schedule update",
        "subtitle": "CodeSphere Hackathon briefing",
        "message": "Problem statements will be unlocked 1 hour prior to hacking. Squad formation portal is now open. Match with teammates in the squad tab!",
        "category": "Update",
        "event_id": "3",
        "date": "Saturday, 26 Nov 2026",
        "time_slot": "9:00 AM - 9:00 PM",
        "venue": "CS Innovation Lab & Maker Space",
        "unread": False
    },
    {
        "id": "notif-4",
        "user_id": "usr-1",
        "title": "Workshop registration",
        "subtitle": "Frontend Sprint: Web UI Masterclass",
        "message": "Seat confirmed for Web UI Masterclass. Please pre-install Node.js and VS Code on your laptop.",
        "category": "Registration",
        "event_id": "4",
        "date": "Wednesday, 02 Dec 2026",
        "time_slot": "2:00 PM - 5:00 PM",
        "venue": "Computer Lab 3 (West Wing)",
        "unread": False
    }
]

BOOKMARKS_SEED = [
    {"user_id": "usr-1", "event_id": "1"},
    {"user_id": "usr-1", "event_id": "2"},
    {"user_id": "usr-1", "event_id": "4"},
    {"user_id": "usr-1", "event_id": "5"}
]
