/**
 * CampusConnect Event Frontend Application
 * Interacts with:
 *   - GET  /api/events
 *   - GET  /api/events/{id}
 *   - POST /api/registrations (201 / 409)
 *   - GET  /api/me/registrations
 *   - GET  /api/events/{id}/registrations
 */

// Application State
const state = {
  activeScreen: 1, // 1 to 12 matching the Figma screens
  events: [],
  myRegistrations: [],
  currentEvent: null,
  activeRegistration: null,
  selectedCategory: 'All',
  searchQuery: '',
  calendarMonth: 10, // November (0-indexed 10 = Nov)
  calendarYear: 2026,
  selectedCalendarDay: 12,
  user: {
    name: 'Anwitha Guntupalli',
    email: 'anwitha@campus.edu',
    phone: '+91 98765 43210',
    department: 'Computer Science & Technology',
    grade: '3rd Year CS',
    student_id: 'STU-2024-CS-094',
    saved_event_ids: ['1', '2', '4', '5'],
    interests: ['AI & ML', 'Web Dev', 'Design', 'Leadership']
  },
  notifications: [
    {
      id: 'notif-1',
      title: 'Registration confirmed',
      subtitle: 'AI & the Future Tech Talk',
      time: '2 hours ago',
      unread: true,
      category: 'Registration',
      event_id: '1',
      date: 'Thursday, 12 Nov 2026',
      time_slot: '10:00 AM - 12:00 PM',
      venue: 'Main Auditorium Hall A',
      message: "You're registered for AI & the Future Tech Talk! Please arrive 15 minutes before session commencement with your digital event pass for priority scan-in."
    },
    {
      id: 'notif-2',
      title: 'Event reminder',
      subtitle: 'Aura Cultural Fest Gala',
      time: 'Yesterday',
      unread: false,
      category: 'Reminder',
      event_id: '2',
      date: 'Friday, 19 Nov 2026',
      time_slot: '4:00 PM - 10:00 PM',
      venue: 'Campus Amphitheatre',
      message: 'Aura Cultural Fest schedule has been published! Musical band lineup begins at 6 PM. Check-in wristbands available from 3:30 PM at the main gates.'
    },
    {
      id: 'notif-3',
      title: 'Schedule update',
      subtitle: 'CodeSphere Hackathon briefing',
      time: '2 days ago',
      unread: false,
      category: 'Update',
      event_id: '3',
      date: 'Saturday, 26 Nov 2026',
      time_slot: '9:00 AM - 9:00 PM',
      venue: 'CS Innovation Lab & Maker Space',
      message: 'Problem statements will be unlocked 1 hour prior to hacking. Squad formation portal is now open. Match with teammates in the squad tab!'
    },
    {
      id: 'notif-4',
      title: 'Workshop registration',
      subtitle: 'Frontend Sprint: Web UI Masterclass',
      time: '3 days ago',
      unread: false,
      category: 'Registration',
      event_id: '4',
      date: 'Wednesday, 02 Dec 2026',
      time_slot: '2:00 PM - 5:00 PM',
      venue: 'Computer Lab 3 (West Wing)',
      message: 'Seat confirmed for Web UI Masterclass. Please pre-install Node.js and VS Code on your laptop.'
    }
  ],
  selectedNotification: null,
  coBuilders: [
    {
      id: 'cb-1',
      name: 'Riya Sharma',
      role: 'Frontend Developer',
      skills: ['React', 'Tailwind', 'TypeScript', 'Next.js'],
      avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120',
      matchScore: '96%',
      status: 'Available',
      invited: false
    },
    {
      id: 'cb-2',
      name: 'Aman Kumar',
      role: 'Backend & Systems Engineer',
      skills: ['Python', 'FastAPI', 'PostgreSQL', 'Docker'],
      avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120',
      matchScore: '92%',
      status: 'Looking for AI/Web squad',
      invited: false
    },
    {
      id: 'cb-3',
      name: 'Meera Patel',
      role: 'UI/UX & Product Designer',
      skills: ['Figma', 'Wireframing', 'User Research', 'Design Systems'],
      avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120',
      matchScore: '88%',
      status: 'Open to Hackathons',
      invited: false
    },
    {
      id: 'cb-4',
      name: 'Devin Chen',
      role: 'ML & Data Engineer',
      skills: ['PyTorch', 'Vector DBs', 'LLMs', 'LangChain'],
      avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120',
      matchScore: '85%',
      status: 'Available',
      invited: false
    }
  ],
  organizerStats: {
    publishedEvents: 8,
    totalRegistrations: 486,
    turnoutRate: '76%',
    pendingRequests: 42
  },
  attendeeModalEvent: null,
  attendeeList: []
};

// Seed Fallback Events
const SEED_EVENTS = [
  {
    id: "1",
    slug: "ai-and-the-future",
    title: "AI & the Future",
    tag: "TECH TALK",
    category: "Tech",
    interests: ["AI & ML", "Web Dev"],
    hero_badge: "TECH TALK",
    date: "12 Nov 2026",
    day: "Thu",
    time: "10:00 AM - 12:00 PM",
    location: "Main Auditorium Hall A",
    organizer: "AI Club (Tech Club)",
    price: "Free Entry",
    price_val: 0,
    is_featured: true,
    badge_color: "blue",
    icon: "cpu",
    short_desc: "A practical inspiring talk with founders and engineers building real AI.",
    description: "Discover how large language models, agentic workflows, and multimodal systems are reshaping product development. Join leading researchers and student builders as they demo autonomous systems and discuss career pathways in modern AI engineering.",
    perks: [
      "Networking session pass with AI founders",
      "Hands-on code demo repository & sample files",
      "Official certificate of participation",
      "Live Q&A and hardware demo showcase"
    ],
    registered_count: 142,
    capacity: 200,
    status: "Active"
  },
  {
    id: "2",
    slug: "aura-cultural-fest",
    title: "Aura Cultural Fest",
    tag: "CULTURE",
    category: "Culture",
    interests: ["Design", "Leadership"],
    hero_badge: "CULTURAL GALA",
    date: "19 Nov 2026",
    day: "Fri",
    time: "4:00 PM - 10:00 PM",
    location: "Campus Amphitheatre",
    organizer: "Cultural Arts Council",
    price: "Free Entry",
    price_val: 0,
    is_featured: true,
    badge_color: "rose",
    icon: "sparkles",
    short_desc: "Annual inter-college cultural gala featuring live musical bands & art showcases.",
    description: "Experience an electric evening celebrating youth culture, performing arts, acoustic indie bands, and student dance showcases. Grab food truck specials and participate in campus-wide open-mic spotlights.",
    perks: [
      "Festival wristband & glow accessories",
      "Front-stage access voucher",
      "Campus food stall discount vouchers",
      "Entry to evening celebrity performance"
    ],
    registered_count: 310,
    capacity: 500,
    status: "Active"
  },
  {
    id: "3",
    slug: "codesphere-hackathon",
    title: "CodeSphere Hackathon",
    tag: "HACKATHON",
    category: "Tech",
    interests: ["AI & ML", "Web Dev", "Leadership"],
    hero_badge: "24H HACKATHON",
    date: "26 Nov 2026",
    day: "Sat",
    time: "9:00 AM - 9:00 PM",
    location: "CS Innovation Lab & Maker Space",
    organizer: "Developer Student Guild (Tech Club)",
    price: "Free Entry",
    price_val: 0,
    is_featured: true,
    badge_color: "violet",
    icon: "code",
    short_desc: "Build something incredible in 24 hours with AI, web, and mobile tech.",
    description: "Assemble your team or match with fellow builders on campus. Tackle industry problem statements across healthcare, education, sustainability, and generative tools. $10,000+ in sponsor prize pools, API credits, and venture mentor evaluations.",
    perks: [
      "Exclusive CodeSphere participant kit & swag hoodie",
      "Complimentary meals, energy snacks & midnight pizza",
      "Cloud hosting credits & API access tokens",
      "1-on-1 mentorship with senior engineering leads"
    ],
    registered_count: 210,
    capacity: 250,
    status: "Active"
  },
  {
    id: "4",
    slug: "frontend-sprint",
    title: "Frontend Sprint: Web UI Masterclass",
    tag: "WORKSHOP",
    category: "Workshops",
    interests: ["Web Dev", "Design"],
    hero_badge: "HANDS-ON WORKSHOP",
    date: "02 Dec 2026",
    day: "Wed",
    time: "2:00 PM - 5:00 PM",
    location: "Computer Lab 3 (West Wing)",
    organizer: "Web Dev Society",
    price: "Free Entry",
    price_val: 0,
    is_featured: false,
    badge_color: "blue",
    icon: "layout",
    short_desc: "Level up modern web architecture, CSS animations, and design system engineering.",
    description: "Learn how modern frontend engineering bridges Figma design tokens with high-performance components. We'll build real reactive micro-interactions, responsive grids, and accessible components.",
    perks: [
      "Starter repo & design system component kit",
      "Lab workstation access",
      "Peer code review session"
    ],
    registered_count: 78,
    capacity: 90,
    status: "Active"
  },
  {
    id: "5",
    slug: "design-jam-for-good",
    title: "Design Jam: UI/UX for Good",
    tag: "DESIGN",
    category: "Career",
    interests: ["Design", "Leadership"],
    hero_badge: "CREATIVE SPRINT",
    date: "05 Dec 2026",
    day: "Sat",
    time: "11:00 AM - 4:00 PM",
    location: "Design Studio B, Faculty of Arts",
    organizer: "Design Collective",
    price: "Free Entry",
    price_val: 0,
    is_featured: false,
    badge_color: "amber",
    icon: "pen-tool",
    short_desc: "Design intuitive user flows and prototypes tackling social impact challenges.",
    description: "A collaborative design sprint pairing designers and product strategists to redesign civic tech services, environmental tracking, and accessible campus tools.",
    perks: [
      "Figma community template pack",
      "Design critique with industry designers",
      "Portfolio showcase opportunity"
    ],
    registered_count: 64,
    capacity: 80,
    status: "Active"
  },
  {
    id: "6",
    slug: "deep-learning-workshop",
    title: "Deep Learning & PyTorch Primer",
    tag: "WORKSHOP",
    category: "Workshops",
    interests: ["AI & ML"],
    hero_badge: "HANDS-ON LAB",
    date: "15 Dec 2026",
    day: "Tue",
    time: "1:00 PM - 4:30 PM",
    location: "Seminar Hall 2 & Cloud GPU Lab",
    organizer: "AI Club (Tech Club)",
    price: "Free Entry",
    price_val: 0,
    is_featured: false,
    badge_color: "indigo",
    icon: "cpu",
    short_desc: "From linear models to neural networks with live GPU execution.",
    description: "Deep-dive into tensor operations, backpropagation, and training your first convolutional and transformer architectures using PyTorch and Colab Pro GPU clusters.",
    perks: [
      "GPU compute credits",
      "Jupyter notebooks and starter code",
      "Certificate of completion"
    ],
    registered_count: 50,
    capacity: 60,
    status: "Active"
  }
];

// Seed Fallback User Registrations
const SEED_REGISTRATIONS = [
  {
    id: "reg-1",
    event_id: "1",
    user_email: "anwitha@campus.edu",
    user_name: "Anwitha Guntupalli",
    phone: "+91 98765 43210",
    department: "Computer Science & Technology",
    registration_type: "Student Attendee",
    ticket_id: "CC-2026-FUT-0481",
    status: "CONFIRMED",
    created_at: "2026-10-24T10:14:00Z",
    event: SEED_EVENTS[0]
  },
  {
    id: "reg-2",
    event_id: "2",
    user_email: "anwitha@campus.edu",
    user_name: "Anwitha Guntupalli",
    phone: "+91 98765 43210",
    department: "Computer Science & Technology",
    registration_type: "General Access",
    ticket_id: "CC-2026-AUR-1092",
    status: "CONFIRMED",
    created_at: "2026-10-25T14:30:00Z",
    event: SEED_EVENTS[1]
  },
  {
    id: "reg-3",
    event_id: "3",
    user_email: "anwitha@campus.edu",
    user_name: "Anwitha Guntupalli",
    phone: "+91 98765 43210",
    department: "Computer Science & Technology",
    registration_type: "Hackathon Participant",
    ticket_id: "CC-2026-CSH-3380",
    status: "WAITLIST",
    created_at: "2026-10-26T09:00:00Z",
    event: SEED_EVENTS[2]
  }
];

// Screen definitions for quick navigator
const SCREEN_TITLES = {
  1: "1. Explore & Browse (Hero)",
  2: "2. Monthly Calendar & Agenda",
  3: "3. Event Registration Form",
  4: "4. Notification & Email Inbox",
  5: "5. Student Hub / Dashboard",
  6: "6. Event Detail Page (AI & Future)",
  7: "7. My Registrations / Activity",
  8: "8. Digital Event Pass / Ticket",
  9: "9. Tech Club Organizer Dashboard",
  10: "10. Interest Discovery",
  11: "11. Student User Profile",
  12: "12. Co-Builder Squad Matcher"
};

// ======================== API CLIENT ========================

// 1. GET /api/events
async function fetchEvents(category = '', search = '') {
  try {
    const params = new URLSearchParams();
    if (category && category !== 'All') params.append('category', category);
    if (search) params.append('search', search);
    const url = `/api/events${params.toString() ? '?' + params.toString() : ''}`;
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    return data.events || [];
  } catch (err) {
    console.warn("Using local events data fallback:", err.message);
    let filtered = [...SEED_EVENTS];
    if (category && category !== 'All') {
      filtered = filtered.filter(e => e.category.toLowerCase() === category.toLowerCase());
    }
    if (search) {
      const q = search.toLowerCase();
      filtered = filtered.filter(e => e.title.toLowerCase().includes(q) || e.short_desc.toLowerCase().includes(q));
    }
    return filtered;
  }
}

// 2. GET /api/events/{id}
async function fetchEventDetails(eventId) {
  try {
    const res = await fetch(`/api/events/${eventId}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn("Using local event details fallback:", err.message);
    const ev = state.events.find(e => e.id === String(eventId)) || SEED_EVENTS[0];
    const isRegistered = state.myRegistrations.some(r => r.event_id === String(eventId));
    return { ...ev, is_current_user_registered: isRegistered };
  }
}

// 3. POST /api/registrations (201 Created or 409 Conflict)
async function registerForEvent(payload) {
  try {
    const res = await fetch('/api/registrations', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    return { status: res.status, data };
  } catch (err) {
    console.warn("Simulating POST /api/registrations locally:", err.message);
    const eventId = String(payload.event_id);
    const existing = state.myRegistrations.find(
      r => r.event_id === eventId && r.user_email.toLowerCase() === payload.email.toLowerCase()
    );
    if (existing) {
      return {
        status: 409,
        data: {
          error: "Conflict: You are already registered for this event.",
          status: 409,
          existing_registration: existing
        }
      };
    }
    const event = state.events.find(e => e.id === eventId) || SEED_EVENTS[0];
    const newReg = {
      id: `reg-${Date.now()}`,
      event_id: eventId,
      user_email: payload.email,
      user_name: payload.name,
      phone: payload.phone,
      department: payload.department,
      registration_type: payload.registration_type || "Student Attendee",
      ticket_id: `CC-2026-FUT-${Math.floor(1000 + Math.random() * 9000)}`,
      status: "CONFIRMED",
      created_at: new Date().toISOString(),
      event: event
    };
    state.myRegistrations.unshift(newReg);
    event.registered_count += 1;
    return {
      status: 201,
      data: {
        message: "Registration successful!",
        status: 201,
        registration: newReg,
        event: event
      }
    };
  }
}

// 4. GET /api/me/registrations
async function fetchMyRegistrations() {
  try {
    const res = await fetch('/api/me/registrations');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    return data.registrations || [];
  } catch (err) {
    console.warn("Using local registrations fallback:", err.message);
    return state.myRegistrations.length ? state.myRegistrations : [...SEED_REGISTRATIONS];
  }
}

// 5. GET /api/events/{id}/registrations (Organizer Attendee List)
async function fetchEventAttendees(eventId) {
  try {
    const res = await fetch(`/api/events/${eventId}/registrations`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn("Using local attendees fallback:", err.message);
    const ev = state.events.find(e => e.id === String(eventId)) || SEED_EVENTS[0];
    return {
      event: {
        id: ev.id,
        title: ev.title,
        organizer: ev.organizer,
        capacity: ev.capacity,
        registered_count: ev.registered_count
      },
      registrations: [
        {
          id: "reg-1",
          user_name: "Anwitha Guntupalli",
          user_email: "anwitha@campus.edu",
          department: "Computer Science & Technology",
          phone: "+91 98765 43210",
          ticket_id: "CC-2026-FUT-0481",
          status: "CONFIRMED",
          created_at: "2026-10-24T10:14:00Z"
        },
        {
          id: "reg-4",
          user_name: "Riya Sharma",
          user_email: "riya.sharma@campus.edu",
          department: "Information Science",
          phone: "+91 98111 22334",
          ticket_id: "CC-2026-FUT-0482",
          status: "CONFIRMED",
          created_at: "2026-10-24T11:20:00Z"
        },
        {
          id: "reg-5",
          user_name: "Aman Kumar",
          user_email: "aman.kumar@campus.edu",
          department: "Computer Science & Technology",
          phone: "+91 98222 33445",
          ticket_id: "CC-2026-FUT-0483",
          status: "CONFIRMED",
          created_at: "2026-10-24T12:05:00Z"
        },
        {
          id: "reg-6",
          user_name: "Meera Patel",
          user_email: "meera.patel@campus.edu",
          department: "Design & Media",
          phone: "+91 98333 44556",
          ticket_id: "CC-2026-FUT-0484",
          status: "CONFIRMED",
          created_at: "2026-10-24T13:40:00Z"
        },
        {
          id: "reg-7",
          user_name: "Rohit Verma",
          user_email: "rohit.verma@campus.edu",
          department: "Electronics & Comm",
          phone: "+91 98444 55667",
          ticket_id: "CC-2026-FUT-0485",
          status: "CHECKED_IN",
          created_at: "2026-10-24T15:10:00Z"
        }
      ]
    };
  }
}

// ======================== APP CONTROLLER ========================

async function initApp() {
  state.events = await fetchEvents();
  state.myRegistrations = await fetchMyRegistrations();
  state.currentEvent = state.events[0];
  state.activeRegistration = state.myRegistrations[0];
  state.selectedNotification = state.notifications[0];

  renderNavActiveStates();
  renderScreenSwitcherButtons();
  renderCurrentScreen();
  lucide.createIcons();
}

// Switch between screens 1 to 12
function switchScreen(screenNum) {
  state.activeScreen = Number(screenNum);
  window.scrollTo({ top: 0, behavior: 'smooth' });
  renderNavActiveStates();
  renderCurrentScreen();
  updateSwitcherActive();
}

function updateSwitcherActive() {
  document.querySelectorAll('.screen-pill-btn').forEach(btn => {
    const s = Number(btn.getAttribute('data-screen'));
    if (s === state.activeScreen) {
      btn.className = 'screen-pill-btn px-3 py-1.5 text-xs font-semibold rounded-full bg-rose-500 text-white shadow-sm transition whitespace-nowrap';
    } else {
      btn.className = 'screen-pill-btn px-3 py-1.5 text-xs font-medium rounded-full bg-slate-800 text-slate-300 hover:bg-slate-700 transition whitespace-nowrap';
    }
  });
}

function renderNavActiveStates() {
  const s = state.activeScreen;
  const isEvents = (s === 1 || s === 6 || s === 3 || s === 5 || s === 10);
  const isCalendar = (s === 2);
  const isMyRegistrations = (s === 7 || s === 8 || s === 4 || s === 11 || s === 12);
  const isOrganizer = (s === 9);

  const setTab = (id, active) => {
    const el = document.getElementById(id);
    if (!el) return;
    if (active) {
      el.className = 'nav-tab text-sm font-semibold text-rose-500 border-b-2 border-rose-500 pb-1 cursor-pointer transition';
    } else {
      el.className = 'nav-tab text-sm font-medium text-slate-600 hover:text-slate-900 pb-1 cursor-pointer transition';
    }
  };

  setTab('nav-tab-events', isEvents);
  setTab('nav-tab-calendar', isCalendar);
  setTab('nav-tab-myreg', isMyRegistrations);

  // Toggle organizer badge indicator
  const orgBtn = document.getElementById('nav-organizer-btn');
  if (orgBtn) {
    if (isOrganizer) {
      orgBtn.className = 'flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-full bg-slate-900 text-white shadow-sm ring-2 ring-rose-500';
    } else {
      orgBtn.className = 'flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-full bg-slate-100 text-slate-700 hover:bg-slate-200 transition';
    }
  }
}

// Render the 12 floating switcher buttons
function renderScreenSwitcherButtons() {
  const container = document.getElementById('screen-switcher-list');
  if (!container) return;
  container.innerHTML = '';
  for (let i = 1; i <= 12; i++) {
    const btn = document.createElement('button');
    btn.setAttribute('data-screen', i);
    btn.textContent = SCREEN_TITLES[i];
    btn.onclick = () => switchScreen(i);
    btn.className = (i === state.activeScreen)
      ? 'screen-pill-btn px-3 py-1.5 text-xs font-semibold rounded-full bg-rose-500 text-white shadow-sm transition whitespace-nowrap'
      : 'screen-pill-btn px-3 py-1.5 text-xs font-medium rounded-full bg-slate-800 text-slate-300 hover:bg-slate-700 transition whitespace-nowrap';
    container.appendChild(btn);
  }
}

// Main screen router
function renderCurrentScreen() {
  const container = document.getElementById('app-main-content');
  if (!container) return;

  // Hide all screens
  for (let i = 1; i <= 12; i++) {
    const el = document.getElementById(`screen-${i}`);
    if (el) el.classList.add('hidden');
  }

  // Show active screen
  const activeEl = document.getElementById(`screen-${state.activeScreen}`);
  if (activeEl) {
    activeEl.classList.remove('hidden');
  }

  // Refresh dynamic parts of the screen
  if (state.activeScreen === 1) renderScreen1();
  if (state.activeScreen === 2) renderScreen2();
  if (state.activeScreen === 3) renderScreen3();
  if (state.activeScreen === 4) renderScreen4();
  if (state.activeScreen === 5) renderScreen5();
  if (state.activeScreen === 6) renderScreen6();
  if (state.activeScreen === 7) renderScreen7();
  if (state.activeScreen === 8) renderScreen8();
  if (state.activeScreen === 9) renderScreen9();
  if (state.activeScreen === 10) renderScreen10();
  if (state.activeScreen === 11) renderScreen11();
  if (state.activeScreen === 12) renderScreen12();

  setTimeout(() => lucide.createIcons(), 50);
}

// ======================== SCREEN RENDERERS ========================

// SCREEN 1: Explore & Browse Events
function renderScreen1() {
  renderCategoryFilterChips();
  renderFeaturedEvents();
  renderAllEventsGrid();
}

function renderCategoryFilterChips() {
  const categories = ['All', 'Tech', 'Culture', 'Workshops', 'Career', 'Sports'];
  const container = document.getElementById('s1-filter-chips');
  if (!container) return;
  container.innerHTML = categories.map(cat => {
    const isSel = state.selectedCategory === cat;
    return `
      <button onclick="handleCategoryFilter('${cat}')"
        class="px-4 py-2 text-xs font-semibold rounded-full transition-all ${
          isSel
            ? 'bg-slate-900 text-white shadow-sm'
            : 'bg-white text-slate-600 border border-slate-200 hover:border-slate-300 hover:text-slate-900'
        }">
        ${cat}
      </button>
    `;
  }).join('');
}

async function handleCategoryFilter(category) {
  state.selectedCategory = category;
  renderCategoryFilterChips();
  state.events = await fetchEvents(state.selectedCategory, state.searchQuery);
  renderAllEventsGrid();
  lucide.createIcons();
}

async function handleSearchInput(value) {
  state.searchQuery = value.trim();
  state.events = await fetchEvents(state.selectedCategory, state.searchQuery);
  renderAllEventsGrid();
  lucide.createIcons();
}

function renderFeaturedEvents() {
  const container = document.getElementById('s1-featured-grid');
  if (!container) return;
  const featured = state.events.filter(e => e.is_featured).slice(0, 3);

  container.innerHTML = featured.map(ev => {
    let iconClass = "bg-blue-50 text-blue-600";
    let iconName = "cpu";
    if (ev.tag === "CULTURE") {
      iconClass = "bg-rose-50 text-rose-600";
      iconName = "sparkles";
    } else if (ev.tag === "HACKATHON") {
      iconClass = "bg-violet-50 text-violet-600";
      iconName = "code-2";
    }

    return `
      <div class="hover-card bg-white rounded-3xl p-6 border border-slate-100 shadow-sm flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <div class="w-11 h-11 rounded-2xl ${iconClass} flex items-center justify-center font-bold text-sm">
              <i data-lucide="${iconName}" class="w-5 h-5"></i>
            </div>
            <span class="px-2.5 py-1 text-[11px] font-bold tracking-wider rounded-md uppercase bg-slate-100 text-slate-700">
              ${ev.tag}
            </span>
          </div>
          <h3 class="text-xl font-bold text-slate-900 mb-1.5">${ev.title}</h3>
          <p class="text-xs text-slate-500 line-clamp-2 mb-4">${ev.short_desc}</p>
        </div>

        <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
          <div class="text-xs text-slate-500">
            <span class="font-semibold text-slate-700">${ev.day}, ${ev.date.split(' ')[0]} ${ev.date.split(' ')[1]}</span>
            <span class="mx-1">•</span>
            <span>${ev.time.split('-')[0].trim()}</span>
          </div>
          <button onclick="goToEventDetails('${ev.id}')"
            class="px-4 py-2 text-xs font-semibold rounded-xl bg-rose-500 hover:bg-rose-600 text-white shadow-sm transition flex items-center gap-1.5">
            <span>View event</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function renderAllEventsGrid() {
  const container = document.getElementById('s1-all-events-grid');
  if (!container) return;
  if (!state.events.length) {
    container.innerHTML = `
      <div class="col-span-full py-16 text-center text-slate-400">
        <i data-lucide="calendar-x" class="w-12 h-12 mx-auto mb-3 opacity-40"></i>
        <p class="text-sm font-medium">No events matching "${state.searchQuery || state.selectedCategory}".</p>
      </div>
    `;
    return;
  }

  container.innerHTML = state.events.map(ev => {
    const isSaved = state.user.saved_event_ids.includes(ev.id);
    return `
      <div class="hover-card bg-white rounded-3xl p-6 border border-slate-100 shadow-sm flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="px-2.5 py-1 text-[11px] font-bold tracking-wide rounded-md uppercase ${
              ev.category === 'Tech' ? 'bg-blue-50 text-blue-600' :
              ev.category === 'Culture' ? 'bg-rose-50 text-rose-600' :
              ev.category === 'Workshops' ? 'bg-emerald-50 text-emerald-600' : 'bg-amber-50 text-amber-600'
            }">
              ${ev.tag}
            </span>
            <button onclick="toggleBookmark('${ev.id}')" class="p-1.5 rounded-full hover:bg-slate-100 text-slate-400 hover:text-rose-500 transition">
              <i data-lucide="bookmark" class="w-4 h-4 ${isSaved ? 'fill-rose-500 text-rose-500' : ''}"></i>
            </button>
          </div>

          <h4 class="text-base font-bold text-slate-900 mb-1 hover:text-rose-600 transition cursor-pointer" onclick="goToEventDetails('${ev.id}')">
            ${ev.title}
          </h4>
          <p class="text-xs text-slate-500 mb-4 line-clamp-2">${ev.short_desc}</p>
        </div>

        <div>
          <div class="flex items-center gap-2 text-xs text-slate-500 mb-4">
            <div class="flex items-center gap-1">
              <i data-lucide="calendar" class="w-3.5 h-3.5 text-slate-400"></i>
              <span>${ev.date}</span>
            </div>
            <span>•</span>
            <div class="flex items-center gap-1">
              <i data-lucide="map-pin" class="w-3.5 h-3.5 text-slate-400"></i>
              <span class="truncate max-w-[120px]">${ev.location.split('(')[0].trim()}</span>
            </div>
          </div>

          <div class="flex items-center justify-between pt-3 border-t border-slate-100">
            <span class="text-xs font-semibold text-emerald-600">${ev.price}</span>
            <button onclick="goToEventDetails('${ev.id}')"
              class="px-3.5 py-1.5 text-xs font-semibold rounded-xl bg-slate-900 text-white hover:bg-rose-600 transition flex items-center gap-1">
              <span>Details</span>
              <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// SCREEN 2: Monthly Calendar & Agenda
function renderScreen2() {
  renderCalendarDaysGrid();
  renderCalendarComingUpList();
}

function renderCalendarDaysGrid() {
  const container = document.getElementById('s2-calendar-grid');
  if (!container) return;

  // Days of November 2026 (Starts on Sunday = Nov 1)
  // Total 30 days
  const eventDays = {
    12: { title: "AI & Future", color: "bg-blue-500" },
    19: { title: "Aura Fest", color: "bg-rose-500" },
    26: { title: "CodeSphere", color: "bg-violet-500" }
  };

  let html = '';
  // Sun(0) to Sat(6)
  // Nov 1 2026 is Sunday, so offset = 0
  for (let day = 1; day <= 30; day++) {
    const hasEvent = eventDays[day];
    const isSelected = day === state.selectedCalendarDay;
    const isToday = day === 29; // Today's date

    html += `
      <div onclick="selectCalendarDay(${day})"
        class="relative min-h-[60px] p-2 rounded-2xl border transition cursor-pointer flex flex-col justify-between ${
          isSelected
            ? 'bg-rose-50 border-rose-400 shadow-sm'
            : isToday
            ? 'bg-slate-50 border-slate-300'
            : 'bg-white border-slate-100 hover:border-slate-200 hover:bg-slate-50/50'
        }">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold ${
            isSelected ? 'text-rose-600' : isToday ? 'text-slate-900 underline' : 'text-slate-700'
          }">${day}</span>
          ${isToday ? '<span class="text-[9px] uppercase font-bold text-rose-500">Today</span>' : ''}
        </div>
        ${
          hasEvent
            ? `<div class="mt-1">
                <div class="w-full truncate px-1.5 py-0.5 rounded text-[10px] font-semibold text-white ${hasEvent.color}">
                  ${hasEvent.title}
                </div>
              </div>`
            : ''
        }
      </div>
    `;
  }
  container.innerHTML = html;
}

function selectCalendarDay(day) {
  state.selectedCalendarDay = day;
  renderCalendarDaysGrid();
  renderCalendarComingUpList();
}

function renderCalendarComingUpList() {
  const container = document.getElementById('s2-coming-up-list');
  if (!container) return;

  container.innerHTML = state.events.slice(0, 4).map(ev => {
    const parts = ev.date.split(' ');
    const day = parts[0];
    const month = parts[1].toUpperCase();

    return `
      <div onclick="goToEventDetails('${ev.id}')"
        class="hover-card p-4 rounded-2xl bg-white border border-slate-100 shadow-sm flex items-center gap-4 cursor-pointer">
        <div class="w-14 h-14 rounded-2xl bg-slate-900 text-white flex flex-col items-center justify-center flex-shrink-0">
          <span class="text-[10px] uppercase font-bold tracking-wider text-rose-400">${month}</span>
          <span class="text-lg font-extrabold leading-none">${day}</span>
        </div>
        <div class="flex-1 min-w-0">
          <h4 class="text-sm font-bold text-slate-900 truncate hover:text-rose-500 transition">${ev.title}</h4>
          <p class="text-xs text-slate-500 truncate">${ev.short_desc}</p>
          <div class="flex items-center gap-2 mt-1 text-[11px] text-slate-400">
            <span>${ev.time}</span>
            <span>•</span>
            <span class="text-rose-500 font-semibold">${ev.tag}</span>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// SCREEN 3: Event Registration Form
function renderScreen3() {
  const ev = state.currentEvent || state.events[0];
  const previewContainer = document.getElementById('s3-event-preview');
  if (previewContainer && ev) {
    previewContainer.innerHTML = `
      <div class="w-14 h-14 rounded-2xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-lg mb-4">
        <i data-lucide="${ev.icon || 'cpu'}" class="w-7 h-7"></i>
      </div>
      <span class="inline-block px-3 py-1 rounded-md text-[11px] font-bold tracking-wider bg-blue-100 text-blue-700 uppercase mb-3">
        ${ev.tag}
      </span>
      <h3 class="text-2xl font-black text-slate-900 mb-2">${ev.title}</h3>
      <p class="text-xs text-slate-500 leading-relaxed mb-6">${ev.short_desc}</p>

      <div class="space-y-3 pt-4 border-t border-slate-100 text-xs text-slate-600">
        <div class="flex items-center gap-2">
          <i data-lucide="calendar" class="w-4 h-4 text-slate-400"></i>
          <span class="font-medium">${ev.day}, ${ev.date}</span>
        </div>
        <div class="flex items-center gap-2">
          <i data-lucide="clock" class="w-4 h-4 text-slate-400"></i>
          <span>${ev.time}</span>
        </div>
        <div class="flex items-center gap-2">
          <i data-lucide="map-pin" class="w-4 h-4 text-slate-400"></i>
          <span>${ev.location}</span>
        </div>
      </div>

      <div class="mt-6 pt-4 border-t border-slate-100 flex items-center justify-between">
        <span class="text-xs text-slate-400">Entry status</span>
        <span class="px-2.5 py-1 text-xs font-bold rounded-full bg-emerald-50 text-emerald-600">${ev.price}</span>
      </div>
    `;
  }

  // Set form defaults from current user
  const nameInput = document.getElementById('reg-form-name');
  const emailInput = document.getElementById('reg-form-email');
  const phoneInput = document.getElementById('reg-form-phone');
  const deptInput = document.getElementById('reg-form-dept');
  if (nameInput) nameInput.value = state.user.name;
  if (emailInput) emailInput.value = state.user.email;
  if (phoneInput) phoneInput.value = state.user.phone;
  if (deptInput) deptInput.value = state.user.department;
}

async function handleRegistrationSubmit(event) {
  event.preventDefault();
  const ev = state.currentEvent || state.events[0];

  const payload = {
    event_id: ev.id,
    name: document.getElementById('reg-form-name').value,
    email: document.getElementById('reg-form-email').value,
    phone: document.getElementById('reg-form-phone').value,
    department: document.getElementById('reg-form-dept').value,
    registration_type: document.getElementById('reg-form-type').value
  };

  const btn = document.getElementById('reg-submit-btn');
  const originalText = btn.innerHTML;
  btn.innerHTML = `<span class="inline-block animate-spin mr-2">⏳</span> Registering...`;
  btn.disabled = true;

  try {
    const response = await registerForEvent(payload);

    if (response.status === 201) {
      showToast("🎉 Registration confirmed! Digital pass generated.", "success");
      state.activeRegistration = response.data.registration;
      // Switch to Digital Pass view (Screen 8)
      setTimeout(() => switchScreen(8), 600);
    } else if (response.status === 409) {
      // 409 Conflict as required by specification!
      showToast("⚠️ Already registered! Found existing reservation for this event.", "warning");
      const existing = state.myRegistrations.find(r => r.event_id === ev.id);
      if (existing) {
        state.activeRegistration = existing;
        setTimeout(() => switchScreen(8), 800);
      }
    } else {
      showToast("Registration failed: " + (response.data.error || "Unknown error"), "error");
    }
  } catch (err) {
    showToast("Error processing registration: " + err.message, "error");
  } finally {
    btn.innerHTML = originalText;
    btn.disabled = false;
  }
}

// SCREEN 4: Notifications & Updates Inbox
function renderScreen4() {
  const listContainer = document.getElementById('s4-notif-list');
  if (listContainer) {
    listContainer.innerHTML = state.notifications.map(notif => {
      const isSel = state.selectedNotification && state.selectedNotification.id === notif.id;
      return `
        <div onclick="selectNotification('${notif.id}')"
          class="p-4 rounded-2xl border transition cursor-pointer flex items-start gap-3 ${
            isSel
              ? 'bg-rose-50/60 border-rose-300 shadow-sm'
              : 'bg-white border-slate-100 hover:border-slate-200'
          }">
          <div class="w-2.5 h-2.5 rounded-full mt-1.5 flex-shrink-0 ${notif.unread ? 'bg-rose-500' : 'bg-transparent'}"></div>
          <div class="flex-1 min-w-0">
            <div class="flex items-center justify-between mb-0.5">
              <h5 class="text-xs font-bold text-slate-900 truncate">${notif.title}</h5>
              <span class="text-[10px] text-slate-400">${notif.time}</span>
            </div>
            <p class="text-xs text-slate-500 truncate">${notif.subtitle}</p>
          </div>
        </div>
      `;
    }).join('');
  }
  renderNotificationPreview();
}

function selectNotification(notifId) {
  state.selectedNotification = state.notifications.find(n => n.id === notifId);
  renderScreen4();
  lucide.createIcons();
}

function renderNotificationPreview() {
  const container = document.getElementById('s4-message-preview');
  if (!container) return;
  const notif = state.selectedNotification || state.notifications[0];

  container.innerHTML = `
    <div class="rounded-3xl border border-slate-200 overflow-hidden bg-white shadow-sm">
      <div class="bg-slate-900 text-white p-5 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-7 h-7 rounded-lg bg-rose-500 flex items-center justify-center font-bold text-xs">CC</div>
          <span class="font-bold text-sm tracking-wide">CampusConnect</span>
        </div>
        <span class="px-2 py-0.5 text-[10px] uppercase font-bold tracking-wider rounded bg-slate-800 text-slate-300">
          ${notif.category}
        </span>
      </div>

      <div class="p-6">
        <div class="mb-4">
          <span class="text-[11px] font-semibold text-rose-500 uppercase tracking-wider">Official Notification</span>
          <h3 class="text-xl font-extrabold text-slate-900 mt-0.5">${notif.title}</h3>
          <p class="text-xs font-semibold text-slate-600">${notif.subtitle}</p>
        </div>

        <p class="text-xs text-slate-600 leading-relaxed bg-slate-50 p-4 rounded-2xl border border-slate-100 mb-6">
          ${notif.message}
        </p>

        <div class="space-y-2 mb-6 text-xs text-slate-600">
          <div class="flex items-center gap-2">
            <i data-lucide="calendar" class="w-4 h-4 text-slate-400"></i>
            <span><strong>Date:</strong> ${notif.date}</span>
          </div>
          <div class="flex items-center gap-2">
            <i data-lucide="clock" class="w-4 h-4 text-slate-400"></i>
            <span><strong>Time:</strong> ${notif.time_slot}</span>
          </div>
          <div class="flex items-center gap-2">
            <i data-lucide="map-pin" class="w-4 h-4 text-slate-400"></i>
            <span><strong>Venue:</strong> ${notif.venue}</span>
          </div>
        </div>

        <div class="flex items-center gap-3 pt-4 border-t border-slate-100">
          <button onclick="goToEventDetails('${notif.event_id}')"
            class="px-4 py-2 text-xs font-semibold rounded-xl bg-rose-500 hover:bg-rose-600 text-white shadow-sm transition">
            View Event Info
          </button>
          <button onclick="switchScreen(8)"
            class="px-4 py-2 text-xs font-semibold rounded-xl bg-slate-900 hover:bg-slate-800 text-white transition">
            Open Digital Pass
          </button>
        </div>
      </div>
    </div>
  `;
}

// SCREEN 5: Student Hub / Dashboard
function renderScreen5() {
  const container = document.getElementById('s5-picked-grid');
  if (!container) return;
  const picked = state.events.slice(0, 3);

  container.innerHTML = picked.map(ev => `
    <div onclick="goToEventDetails('${ev.id}')"
      class="hover-card bg-white p-5 rounded-3xl border border-slate-100 shadow-sm flex items-center gap-4 cursor-pointer">
      <div class="w-12 h-12 rounded-2xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-sm flex-shrink-0">
        <i data-lucide="${ev.icon || 'cpu'}" class="w-5 h-5"></i>
      </div>
      <div class="flex-1 min-w-0">
        <span class="text-[10px] font-bold tracking-wider text-rose-500 uppercase">${ev.tag}</span>
        <h4 class="text-sm font-bold text-slate-900 truncate">${ev.title}</h4>
        <span class="text-xs text-slate-400">${ev.date}</span>
      </div>
      <i data-lucide="chevron-right" class="w-4 h-4 text-slate-300"></i>
    </div>
  `).join('');
}

// SCREEN 6: Event Detail Page
async function renderScreen6() {
  const ev = state.currentEvent || state.events[0];
  if (!ev) return;

  // Fetch full details via GET /api/events/{id}
  const fullDetails = await fetchEventDetails(ev.id);

  // Update hero
  const heroTitle = document.getElementById('s6-title');
  const heroBadge = document.getElementById('s6-badge');
  const heroDateTime = document.getElementById('s6-date-time');
  const descEl = document.getElementById('s6-desc');
  const perksList = document.getElementById('s6-perks-list');
  const regBtn = document.getElementById('s6-reg-btn');

  if (heroTitle) heroTitle.textContent = fullDetails.title;
  if (heroBadge) heroBadge.textContent = fullDetails.tag;
  if (heroDateTime) {
    heroDateTime.textContent = `${fullDetails.date} • ${fullDetails.time} • ${fullDetails.location.toUpperCase()}`;
  }
  if (descEl) descEl.textContent = fullDetails.description;

  if (perksList) {
    perksList.innerHTML = (fullDetails.perks || []).map(p => `
      <li class="flex items-center gap-2.5 text-xs text-slate-600">
        <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-500 flex-shrink-0"></i>
        <span>${p}</span>
      </li>
    `).join('');
  }

  // Sidebar info
  const dateEl = document.getElementById('s6-info-date');
  const timeEl = document.getElementById('s6-info-time');
  const locEl = document.getElementById('s6-info-loc');
  const orgEl = document.getElementById('s6-info-org');
  const capEl = document.getElementById('s6-info-cap');

  if (dateEl) dateEl.textContent = fullDetails.date;
  if (timeEl) timeEl.textContent = fullDetails.time;
  if (locEl) locEl.textContent = fullDetails.location;
  if (orgEl) orgEl.textContent = fullDetails.organizer;
  if (capEl) capEl.textContent = `${fullDetails.registered_count} / ${fullDetails.capacity} registered`;

  if (regBtn) {
    const isRegistered = fullDetails.is_current_user_registered ||
      state.myRegistrations.some(r => r.event_id === fullDetails.id);

    if (isRegistered) {
      regBtn.innerHTML = `<span>View My Digital Pass</span> <i data-lucide="ticket" class="w-4 h-4"></i>`;
      regBtn.className = "w-full py-3.5 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm shadow-sm transition flex items-center justify-center gap-2";
      regBtn.onclick = () => {
        const myReg = state.myRegistrations.find(r => r.event_id === fullDetails.id);
        if (myReg) state.activeRegistration = myReg;
        switchScreen(8);
      };
    } else {
      regBtn.innerHTML = `<span>Register for free</span> <i data-lucide="arrow-right" class="w-4 h-4"></i>`;
      regBtn.className = "w-full py-3.5 px-4 rounded-2xl bg-rose-500 hover:bg-rose-600 text-white font-bold text-sm shadow-sm transition flex items-center justify-center gap-2";
      regBtn.onclick = () => {
        state.currentEvent = fullDetails;
        switchScreen(3);
      };
    }
  }

  lucide.createIcons();
}

function goToEventDetails(eventId) {
  const ev = state.events.find(e => e.id === String(eventId));
  if (ev) state.currentEvent = ev;
  switchScreen(6);
}

// SCREEN 7: My Registrations / Activity
function renderScreen7() {
  const container = document.getElementById('s7-registrations-list');
  if (!container) return;

  if (!state.myRegistrations.length) {
    container.innerHTML = `
      <div class="p-12 text-center text-slate-400 bg-white rounded-3xl border border-slate-100">
        <i data-lucide="ticket" class="w-10 h-10 mx-auto mb-2 opacity-40"></i>
        <p class="text-sm font-medium">You haven't registered for any events yet.</p>
        <button onclick="switchScreen(1)" class="mt-4 px-4 py-2 text-xs font-semibold rounded-xl bg-rose-500 text-white">Explore Events</button>
      </div>
    `;
    return;
  }

  container.innerHTML = state.myRegistrations.map(reg => {
    const ev = reg.event || state.events.find(e => e.id === reg.event_id) || SEED_EVENTS[0];
    const isWaitlist = reg.status === 'WAITLIST';

    return `
      <div class="hover-card bg-white p-5 rounded-3xl border border-slate-100 shadow-sm flex items-center justify-between gap-4">
        <div class="flex items-center gap-4">
          <div class="w-12 h-12 rounded-2xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-sm flex-shrink-0">
            <i data-lucide="${ev.icon || 'cpu'}" class="w-5 h-5"></i>
          </div>
          <div>
            <div class="flex items-center gap-2 mb-1">
              <h4 class="text-base font-bold text-slate-900">${ev.title}</h4>
              <span class="px-2 py-0.5 text-[10px] font-bold rounded-full uppercase ${
                isWaitlist ? 'bg-amber-100 text-amber-700' : 'bg-emerald-100 text-emerald-700'
              }">${reg.status}</span>
            </div>
            <div class="flex items-center gap-3 text-xs text-slate-500">
              <span>${ev.day}, ${ev.date}</span>
              <span>•</span>
              <span>${ev.time.split('-')[0].trim()}</span>
              <span>•</span>
              <span>${ev.location.split('(')[0].trim()}</span>
            </div>
          </div>
        </div>

        <div class="flex items-center gap-2">
          <button onclick="openDigitalPassForReg('${reg.id}')"
            class="px-4 py-2 text-xs font-semibold rounded-xl bg-slate-900 hover:bg-rose-600 text-white transition flex items-center gap-1.5">
            <span>View ticket</span>
            <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function openDigitalPassForReg(regId) {
  const reg = state.myRegistrations.find(r => r.id === regId);
  if (reg) state.activeRegistration = reg;
  switchScreen(8);
}

// SCREEN 8: Digital Event Pass / Ticket
function renderScreen8() {
  const reg = state.activeRegistration || state.myRegistrations[0];
  const ev = reg?.event || state.currentEvent || SEED_EVENTS[0];

  const passTitle = document.getElementById('s8-pass-title');
  const passDate = document.getElementById('s8-pass-date');
  const passTime = document.getElementById('s8-pass-time');
  const passLoc = document.getElementById('s8-pass-loc');
  const passName = document.getElementById('s8-pass-name');
  const passTag = document.getElementById('s8-pass-tag');
  const passTicketId = document.getElementById('s8-pass-ticket-id');

  if (passTitle) passTitle.textContent = ev.title;
  if (passDate) passDate.textContent = `${ev.day}, ${ev.date}`;
  if (passTime) passTime.textContent = ev.time;
  if (passLoc) passLoc.textContent = ev.location;
  if (passName) passName.textContent = (reg?.user_name || state.user.name).toUpperCase();
  if (passTag) passTag.textContent = (ev.tag || "TECH TALK").toUpperCase();
  if (passTicketId) passTicketId.textContent = `ID: ${reg?.ticket_id || 'CC-2026-FUT-0481'}`;

  lucide.createIcons();
}

// SCREEN 9: Organizer Dashboard (Tech Club)
function renderScreen9() {
  const container = document.getElementById('s9-events-table-body');
  if (!container) return;

  container.innerHTML = state.events.map(ev => `
    <tr class="border-b border-slate-100 hover:bg-slate-50/50 transition">
      <td class="py-4 px-4">
        <div class="font-bold text-sm text-slate-900">${ev.title}</div>
        <div class="text-xs text-slate-400">${ev.location}</div>
      </td>
      <td class="py-4 px-4 text-xs text-slate-600 font-medium">${ev.date}</td>
      <td class="py-4 px-4 text-xs font-semibold text-slate-900">${ev.registered_count} / ${ev.capacity}</td>
      <td class="py-4 px-4">
        <span class="px-2.5 py-1 text-[11px] font-bold rounded-full bg-emerald-50 text-emerald-600">Active</span>
      </td>
      <td class="py-4 px-4 text-right">
        <button onclick="openAttendeeModal('${ev.id}')"
          class="px-3 py-1.5 text-xs font-semibold rounded-xl bg-slate-900 hover:bg-rose-500 text-white transition">
          View Attendees
        </button>
      </td>
    </tr>
  `).join('');
}

// Organizer Attendee List Modal (calls GET /api/events/{id}/registrations)
async function openAttendeeModal(eventId) {
  const modal = document.getElementById('attendee-modal');
  const titleEl = document.getElementById('attendee-modal-title');
  const countEl = document.getElementById('attendee-modal-count');
  const listEl = document.getElementById('attendee-modal-list');

  modal.classList.remove('hidden');
  listEl.innerHTML = `<div class="p-6 text-center text-xs text-slate-400">Loading attendee records from /api/events/${eventId}/registrations...</div>`;

  const data = await fetchEventAttendees(eventId);
  state.attendeeModalEvent = data.event;
  state.attendeeList = data.registrations || [];

  if (titleEl) titleEl.textContent = `${data.event.title} • Attendee List`;
  if (countEl) countEl.textContent = `${data.registrations.length} registered attendees`;

  renderAttendeeListRows(state.attendeeList);
  lucide.createIcons();
}

function renderAttendeeListRows(list) {
  const listEl = document.getElementById('attendee-modal-list');
  if (!listEl) return;

  if (!list.length) {
    listEl.innerHTML = `<div class="p-8 text-center text-xs text-slate-400">No attendees registered yet.</div>`;
    return;
  }

  listEl.innerHTML = list.map(item => `
    <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-100 flex items-center justify-between text-xs">
      <div>
        <div class="font-bold text-slate-900">${item.user_name}</div>
        <div class="text-slate-500">${item.user_email} • ${item.department}</div>
      </div>
      <div class="text-right">
        <div class="font-mono font-semibold text-slate-700">${item.ticket_id}</div>
        <span class="inline-block px-2 py-0.5 text-[10px] font-bold rounded-full ${
          item.status === 'CHECKED_IN' ? 'bg-blue-100 text-blue-700' : 'bg-emerald-100 text-emerald-700'
        }">${item.status}</span>
      </div>
    </div>
  `).join('');
}

function closeAttendeeModal() {
  const modal = document.getElementById('attendee-modal');
  if (modal) modal.classList.add('hidden');
}

// SCREEN 10: Made for your interests
function renderScreen10() {
  const chipsContainer = document.getElementById('s10-interest-chips');
  const gridContainer = document.getElementById('s10-cards-grid');

  const interests = ['AI & ML', 'Web Dev', 'Design', 'Leadership', 'Cybersecurity', 'Robotics'];

  if (chipsContainer) {
    chipsContainer.innerHTML = interests.map(i => {
      const active = state.user.interests.includes(i);
      return `
        <button onclick="toggleUserInterest('${i}')"
          class="px-4 py-2 text-xs font-semibold rounded-full transition ${
            active
              ? 'bg-rose-500 text-white shadow-sm'
              : 'bg-white text-slate-600 border border-slate-200 hover:border-slate-300'
          }">
          ${i}
        </button>
      `;
    }).join('');
  }

  if (gridContainer) {
    const recommended = state.events.filter(e =>
      e.interests && e.interests.some(i => state.user.interests.includes(i))
    );

    gridContainer.innerHTML = (recommended.length ? recommended : state.events.slice(0, 3)).map(ev => `
      <div class="hover-card bg-white p-6 rounded-3xl border border-slate-100 shadow-sm flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="px-2.5 py-1 text-[11px] font-bold rounded-md bg-blue-50 text-blue-600 uppercase">${ev.tag}</span>
            <button onclick="toggleBookmark('${ev.id}')" class="text-slate-400 hover:text-rose-500">
              <i data-lucide="bookmark" class="w-4 h-4 ${state.user.saved_event_ids.includes(ev.id) ? 'fill-rose-500 text-rose-500' : ''}"></i>
            </button>
          </div>
          <h4 class="text-base font-bold text-slate-900 mb-1">${ev.title}</h4>
          <p class="text-xs text-slate-500 mb-4 line-clamp-2">${ev.short_desc}</p>
        </div>
        <div class="flex items-center justify-between pt-3 border-t border-slate-100">
          <span class="text-xs text-slate-400">${ev.date}</span>
          <button onclick="goToEventDetails('${ev.id}')"
            class="px-3.5 py-1.5 text-xs font-semibold rounded-xl bg-slate-900 text-white hover:bg-rose-500 transition">
            Explore →
          </button>
        </div>
      </div>
    `).join('');
  }
}

function toggleUserInterest(interest) {
  if (state.user.interests.includes(interest)) {
    state.user.interests = state.user.interests.filter(i => i !== interest);
  } else {
    state.user.interests.push(interest);
  }
  renderScreen10();
  lucide.createIcons();
}

// SCREEN 11: Student User Profile
function renderScreen11() {
  const savedContainer = document.getElementById('s11-saved-list');
  if (!savedContainer) return;

  const saved = state.events.filter(e => state.user.saved_event_ids.includes(e.id));
  if (!saved.length) {
    savedContainer.innerHTML = `<p class="text-xs text-slate-400">No events saved yet. Click bookmark on any event card.</p>`;
    return;
  }

  savedContainer.innerHTML = saved.map(ev => `
    <div class="hover-card p-4 rounded-2xl bg-white border border-slate-100 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center font-bold text-xs">
          <i data-lucide="${ev.icon || 'cpu'}" class="w-4 h-4"></i>
        </div>
        <div>
          <h5 class="text-xs font-bold text-slate-900">${ev.title}</h5>
          <span class="text-[11px] text-slate-400">${ev.date} • ${ev.tag}</span>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <button onclick="goToEventDetails('${ev.id}')" class="px-3 py-1 text-xs font-semibold rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700">View</button>
        <button onclick="toggleBookmark('${ev.id}')" class="text-rose-500 hover:text-slate-400 p-1">
          <i data-lucide="trash-2" class="w-4 h-4"></i>
        </button>
      </div>
    </div>
  `).join('');
}

function toggleBookmark(eventId) {
  if (state.user.saved_event_ids.includes(eventId)) {
    state.user.saved_event_ids = state.user.saved_event_ids.filter(id => id !== eventId);
    showToast("Event removed from saved items", "info");
  } else {
    state.user.saved_event_ids.push(eventId);
    showToast("Event added to saved items ❤️", "success");
  }
  renderCurrentScreen();
  lucide.createIcons();
}

// SCREEN 12: Co-Builder Squad Matcher
function renderScreen12() {
  const container = document.getElementById('s12-matches-grid');
  if (!container) return;

  container.innerHTML = state.coBuilders.map(builder => `
    <div class="hover-card bg-white p-5 rounded-3xl border border-slate-100 shadow-sm flex flex-col justify-between">
      <div>
        <div class="flex items-center gap-3 mb-3">
          <img src="${builder.avatar}" class="w-12 h-12 rounded-2xl object-cover" alt="${builder.name}" />
          <div>
            <h4 class="text-sm font-bold text-slate-900">${builder.name}</h4>
            <p class="text-xs text-slate-500">${builder.role}</p>
          </div>
          <span class="ml-auto px-2 py-0.5 text-[10px] font-bold rounded-full bg-emerald-100 text-emerald-700">
            ${builder.matchScore}
          </span>
        </div>

        <div class="flex flex-wrap gap-1.5 mb-4">
          ${builder.skills.map(s => `
            <span class="px-2 py-0.5 text-[10px] rounded-md bg-slate-100 text-slate-600 font-medium">${s}</span>
          `).join('')}
        </div>
      </div>

      <button onclick="toggleInviteSquad('${builder.id}')"
        class="w-full py-2.5 text-xs font-semibold rounded-xl transition flex items-center justify-center gap-1.5 ${
          builder.invited
            ? 'bg-emerald-50 text-emerald-700 border border-emerald-200'
            : 'bg-slate-900 hover:bg-rose-500 text-white'
        }">
        <i data-lucide="${builder.invited ? 'check' : 'user-plus'}" class="w-3.5 h-3.5"></i>
        <span>${builder.invited ? 'Invitation Sent' : 'Invite to Squad'}</span>
      </button>
    </div>
  `).join('');
}

function toggleInviteSquad(builderId) {
  const builder = state.coBuilders.find(b => b.id === builderId);
  if (!builder) return;
  builder.invited = !builder.invited;
  showToast(
    builder.invited ? `Invite sent to ${builder.name}! 🚀` : `Invite cancelled for ${builder.name}`,
    builder.invited ? "success" : "info"
  );
  renderScreen12();
  lucide.createIcons();
}

// Global Toast Banner
function showToast(message, type = 'info') {
  const toast = document.getElementById('global-toast');
  const toastText = document.getElementById('global-toast-text');
  const toastIcon = document.getElementById('global-toast-icon');
  if (!toast || !toastText) return;

  toastText.textContent = message;

  let bgClass = "bg-slate-900 text-white";
  let iconName = "info";
  if (type === 'success') {
    bgClass = "bg-emerald-600 text-white";
    iconName = "check-circle";
  } else if (type === 'warning') {
    bgClass = "bg-amber-600 text-white";
    iconName = "alert-triangle";
  } else if (type === 'error') {
    bgClass = "bg-rose-600 text-white";
    iconName = "alert-circle";
  }

  toast.className = `fixed top-6 right-6 z-50 px-5 py-3 rounded-2xl shadow-xl flex items-center gap-3 toast-animation ${bgClass}`;
  if (toastIcon) toastIcon.setAttribute('data-lucide', iconName);

  toast.classList.remove('hidden');
  lucide.createIcons();

  clearTimeout(toast._timeout);
  toast._timeout = setTimeout(() => {
    toast.classList.add('hidden');
  }, 4000);
}

// Add to Calendar helper
function handleAddToCalendar() {
  const ev = state.currentEvent || SEED_EVENTS[0];
  showToast(`📅 Added "${ev.title}" to calendar!`, 'success');
}

// Window Onload Initialization
window.addEventListener('DOMContentLoaded', () => {
  initApp();
});
