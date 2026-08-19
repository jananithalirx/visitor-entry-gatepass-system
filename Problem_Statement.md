## 1. Title
Visitor Entry & Gate Pass Management System

## 2. Domain
Facility / Office Security & Administration

## 3. Who is the user? (2-3 user types, with roles)
- **Visitor** — an external person visiting the organization who registers their details and receives a gate pass for a specific host/purpose/time window.
- **Employee / Host** — an internal staff member who is being visited; raises or approves visit requests for their visitors.
- **Admin / Security Staff** — front-desk/security personnel who verify visitor identity, approve or reject gate passes, log entry/exit at the gate, and monitor the visitor dashboard for suspicious activity.

## 4. What problem are we solving? (3-5 sentences, real-life example)
Most small-to-mid-sized offices, colleges, and gated communities still track visitor entries using a physical paper register at the security desk — details are handwritten, illegible, easy to falsify, and impossible to search or audit later. For example, if a security incident occurs and the admin needs to know "who visited Employee X between 2 PM and 4 PM last Tuesday," a paper log makes this nearly impossible to answer quickly. There is also no way to flag a visitor who has overstayed their approved time, was denied entry multiple times, or is attempting entry outside normal visiting hours. This project digitizes the entire visitor lifecycle — registration, host approval, gate pass issuance, and entry/exit logging — while adding an intelligent layer to automatically flag unusual or risky visitor activity that a manual process would miss.

## 5. Proposed Solution (what the application will do, feature-wise)
- Visitor self-registration (name, phone, photo, ID proof reference, purpose of visit, host to meet)
- Host/Employee dashboard to approve or reject incoming visit requests
- Auto-generated digital Gate Pass (QR code) with validity window (valid_from / valid_to) upon approval
- Security/Admin dashboard to scan/verify gate pass and log entry & exit timestamps at the gate
- Real-time visitor status view (Pending / Approved / Checked-In / Checked-Out / Expired / Rejected)
- Blacklist/watchlist management for flagged visitors
- Email/SMS notification to host when their visitor arrives (3rd-party integration)
- **AI/DS Enhancement (Day 42–60):** Anomaly detection model that flags irregular visitor activity — e.g. overstaying beyond pass validity, entry attempts outside normal hours, repeated rejected attempts by the same visitor, or entry logged without a corresponding exit — surfaced on the security dashboard as risk alerts.

## 6. Core Entities / Database Tables (list all, minimum 5)
1. **Visitor** — visitor_id (PK), name, phone, email, id_proof_type, id_proof_number, photo_url
2. **Employee/Host** — employee_id (PK), name, email, department, designation
3. **GatePass** — pass_id (PK), visitor_id (FK), host_id (FK), purpose, valid_from, valid_to, status, qr_code
4. **EntryLog** — log_id (PK), pass_id (FK), gate/checkpoint, entry_time, exit_time
5. **AdminSecurityStaff** — staff_id (PK), name, email, role, assigned_gate
6. **Blacklist/FlaggedVisitor** — flag_id (PK), visitor_id (FK), reason, flagged_by (FK → staff_id), flagged_at
7. **AnomalyAlert** *(populated by the AI module)* — alert_id (PK), pass_id (FK), alert_type, severity, detected_at, resolved (boolean)

Relationships: Visitor 1—N GatePass, Employee 1—N GatePass (as host), GatePass 1—N EntryLog (rare re-entries), Visitor 1—N Blacklist entries, GatePass 1—N AnomalyAlert.

## 7. User Roles & Permissions (minimum 2 distinct roles, e.g. Admin & User)
- **Visitor**: can register self, view own pass status — no access to any dashboard or other visitor's data.
- **Employee/Host**: can view/approve/reject visit requests addressed to them, view their own visit history — cannot access security dashboard, blacklist, or other hosts' requests.
- **Admin/Security Staff**: full access — approve/override passes, log entry/exit, manage blacklist, view all anomaly alerts and dashboards, manage employee records.

## 8. Success Criteria (e.g. 'a user should be able to book an appointment in under 1 minute')
- A visitor should be able to complete registration and request a gate pass in under 2 minutes.
- Security staff should be able to verify and check in a visitor (scan pass → log entry) in under 15 seconds.
- The host should receive an arrival notification (email/SMS) within 30 seconds of visitor check-in.
- The anomaly detection module should flag an overstaying visitor or an off-hours entry attempt automatically, without manual review, within the same session.

## 9. Out of Scope (clearly list what you will NOT build, to avoid over-commitment)
- No physical hardware integration (biometric scanners, RFID turnstiles, CCTV facial recognition) — QR-based digital pass only.
- No native mobile app — responsive web app (React) only.
- No payment/billing module (visitor management is not a paid service in this scope).
- No multi-organization/multi-tenant support — single organization/campus only.
- No real-time video monitoring — anomaly detection works on log/entry data patterns, not video feeds.

## 10. Chosen Track: Python (FastAPI)