
import SwiftUI

// Model for mood entries
struct MoodEntry: Identifiable {
    let id = UUID()
    let mood: String
}

// Model for peer groups
class PeerGroup: ObservableObject, Identifiable {
    var id = UUID()
    var name: String
    @Published var members: [String]

    init(name: String, members: [String]) {
        self.name = name
        self.members = members
    }
}


// Model for teletherapy schedules
struct TeletherapySchedule: Identifiable {
    let id = UUID()
    let date: String
    let time: String
    let duration: String
}

// Model for appointments
struct Appointment: Identifiable {
    let id = UUID()
    let date: String
    let time: String
    let duration: String
}

class UserData: ObservableObject {
    @Published var moodEntries: [MoodEntry] = []
    @Published var peerGroups: [PeerGroup] = []
    @Published var teletherapySchedules: [TeletherapySchedule] = []
    @Published var appointments: [Appointment] = []
    @Published var appointmentTime: String = ""
    @Published var appointmentDuration: String = ""
}

struct ContentView: View {
    @State internal var username = ""
    @State internal var password = ""
    @State private var isShowingDashboard = false
    @State internal var isLoggedIn = false  // Track user login state
    @State internal var isShowingAlert = false
    @State internal var alertTitle = ""
    @State internal var alertMessage = ""
    @ObservedObject var userData = UserData()
    
    var body: some View {
        NavigationView {
            VStack {
                TextField("Username", text: $username)
                    .padding()
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                SecureField("Password", text: $password)
                    .padding()
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                Button("Login") {
                    loginAction()
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
                .sheet(isPresented: $isShowingDashboard) {
                    DashboardView()
                }
                
                NavigationLink(
                    destination: RegistrationView(),
                    label: {
                        Text("Register")
                            .padding()
                            .background(Color.green)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                )
                
                NavigationLink(
                    destination: MoodTrackingView(),
                    label: {
                        Text("Mood Tracking")
                            .padding()
                            .background(Color.orange)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                )
                
                NavigationLink(
                    destination: GroupManagementView(),
                    label: {
                        Text("Group Management")
                            .padding()
                            .background(Color.purple)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                )
                
                NavigationLink(
                    destination: TeletherapyView(),
                    label: {
                        Text("Teletherapy")
                            .padding()
                            .background(Color.red)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                )
                
                NavigationLink(
                    destination: ProfileView()) {
                        Text("Profile")
                            .padding()
                            .background(Color.pink)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                
                NavigationLink(
                    destination: GroupChatView(group: userData.peerGroups.first(where: { $0.name == "Sample Group" }) ?? PeerGroup(name: "Sample Group", members: []))) {
                        Text("Group Chat")
                            .padding()
                            .background(Color.yellow)
                            .foregroundColor(.black)
                            .cornerRadius(10)
                    }
                
                
                NavigationLink(
                    destination: AppointmentView(userData: UserData())) {
                        Text("Appointments")
                            .padding()
                            .background(Color.teal)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                
                NavigationLink(
                    destination: SettingsView()) {
                        Text("Settings")
                            .padding()
                            .background(Color.gray)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                
                NavigationLink(
                    destination: NotificationsView()) {
                        Text("Notifications")
                            .padding()
                            .background(Color.orange)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                
                NavigationLink(
                    destination: FeedbackView()) {
                        Text("Feedback")
                            .padding()
                            .background(Color.red)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
                
                NavigationLink(
                    destination: SecurityView()) {
                        Text("Security")
                            .padding()
                            .background(Color.black)
                            .foregroundColor(.white)
                            .cornerRadius(10)
                    }
            }
            .padding()
            .navigationTitle("Login/Register")
        }
    }
    
    // Helper function to show an alert
    private func showAlert(title: String, message: String) {
        // implement an alert here
        print("Alert: \(title) - \(message)")
    }
    
    // Login action
    internal func loginAction() {
        // Implement login logic
        if username == "user" && password == "password" {
            isLoggedIn = true
            isShowingDashboard = true
        } else {
            // Show an alert for invalid credentials
            showAlert(title: "Invalid Credentials", message: "Please check your username and password.")
        }
    }
    
    // Register action
    internal func registerAction() {
        // Implement registration logic
    }
    
    internal struct RegistrationView: View {
        @State internal var username = ""
        @State internal var password = ""
        @State internal var isShowingAlert = false
        @State internal var alertTitle = ""
        @State internal var alertMessage = ""
        
        var body: some View {
            NavigationView {
                VStack {
                    TextField("Username", text: $username)
                        .padding()
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    SecureField("Password", text: $password)
                        .padding()
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Button("Register") {
                        registerAction()
                    }
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
                    
                    NavigationLink(
                        destination: DashboardView(),
                        label: {
                            Text("Continue to Dashboard")
                                .padding()
                                .background(Color.blue)
                                .foregroundColor(.white)
                                .cornerRadius(10)
                        }
                    )
                }
                .padding()
                .navigationTitle("Register")
                .alert(isPresented: $isShowingAlert) {
                    Alert(title: Text(alertTitle), message: Text(alertMessage), dismissButton: .default(Text("OK")))
                }
            }
        }
        
        internal func showAlert(title: String, message: String) {
            alertTitle = title
            alertMessage = message
            isShowingAlert = true
        }
        // Register action
        internal func registerAction() {
            // Implement registration logic
            if !username.isEmpty && !password.isEmpty {
                // You can perform user registration here
                // For simplicity, just print registration details
                print("Registered: \(username), \(password)")
            } else {
                // Show an alert for missing credentials
                showAlert(title: "Incomplete Registration", message: "Please fill in all fields.")
            }
        }
    }
    
    struct DashboardView: View {
        var body: some View {
            NavigationView {
                VStack {
                    Text("Welcome to the Dashboard!")
                        .padding()
                    
                    NavigationLink(
                        destination: MoodTrackingView(),
                        label: {
                            Text("Mood Tracking")
                                .padding()
                                .background(Color.orange)
                                .foregroundColor(.white)
                                .cornerRadius(10)
                        }
                    )
                    
                    NavigationLink(
                        destination: GroupManagementView(),
                        label: {
                            Text("Group Management")
                                .padding()
                                .background(Color.purple)
                                .foregroundColor(.white)
                                .cornerRadius(10)
                        }
                    )
                    
                    NavigationLink(
                        destination: TeletherapyView(),
                        label: {
                            Text("Teletherapy")
                                .padding()
                                .background(Color.red)
                                .foregroundColor(.white)
                                .cornerRadius(10)
                        }
                    )
                }
                .padding()
                .navigationTitle("Dashboard")
            }
        }
    }
    
    struct MoodTrackingView: View {
        @ObservedObject var userData: UserData = UserData()
        @State private var mood = ""
        
        var body: some View {
            NavigationView {
                VStack {
                    TextField("Enter Mood", text: $mood)
                        .padding()
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Button("Log Mood") {
                        userData.moodEntries.append(MoodEntry(mood: mood))
                        mood = ""
                    }
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
                    
                    List {
                        ForEach(userData.moodEntries) { entry in
                            Text(entry.mood)
                        }
                    }
                }
                .padding()
                .navigationTitle("Mood Tracking")
            }
        }
    }
    
    struct GroupManagementView: View {
        @ObservedObject var userData: UserData = UserData()
        @State private var groupName = ""
        
        var body: some View {
            NavigationView {
                VStack {
                    TextField("Enter Group Name", text: $groupName)
                        .padding()
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Button("Create Group") {
                        userData.peerGroups.append(PeerGroup(name: groupName, members: []))
                        groupName = ""
                    }
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
                    
                    List {
                        ForEach(userData.peerGroups) { group in
                            NavigationLink(
                                destination: GroupDetailView(groupIndex: userData.peerGroups.firstIndex(where: { $0.id == group.id }) ?? 0, userData: userData),
                                label: {
                                    Text(group.name)
                                }
                            )
                        }
                    }
                }
                .padding()
                .navigationTitle("Group Management")
            }
        }
    }
    
    
    struct GroupDetailView: View {
        var groupIndex: Int
        @ObservedObject var userData: UserData
        @State private var newMember = ""
        
        var body: some View {
            VStack {
                List {
                    ForEach(userData.peerGroups[groupIndex].members, id: \.self) { member in
                        Text(member)
                    }
                }
                
                TextField("Enter Username", text: $newMember)
                    .padding()
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                Button("Add Member") {
                    if !newMember.isEmpty {
                        if !userData.peerGroups[groupIndex].members.contains(newMember) {
                            userData.peerGroups[groupIndex].members.append(newMember)
                            newMember = ""
                        }
                    }
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
            .padding()
            .navigationTitle(userData.peerGroups[groupIndex].name)
        }
    }
    
    struct TeletherapyView: View {
        @ObservedObject var userData: UserData = UserData()
        @State private var date = ""
        @State private var time = ""
        @State private var duration = ""
        
        var body: some View {
            NavigationView {
                VStack {
                    TextField("Enter Date", text: $date)
                        .padding()
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    TextField("Enter Time", text: $time)
                        .padding()
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    TextField("Enter Duration (minutes)", text: $duration)
                        .padding()
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Button("Schedule Teletherapy") {
                        userData.teletherapySchedules.append(TeletherapySchedule(date: date, time: time, duration: duration))
                        date = ""
                        time = ""
                        duration = ""
                    }
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
                    
                    List {
                        ForEach(userData.teletherapySchedules) { schedule in
                            Text("\(schedule.date) at \(schedule.time), \(schedule.duration) minutes")
                        }
                    }
                }
                .padding()
                .navigationTitle("Teletherapy")
            }
        }
    }
    
    struct ProfileView: View {
        @State private var fullName = ""
        @State private var email = ""
        
        var body: some View {
            VStack {
                TextField("Full Name", text: $fullName)
                    .padding()
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                TextField("Email", text: $email)
                    .padding()
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                Button("Update Profile") {
                    // Implement logic to update user profile
                    // Use fullName and email
                    print("Updated Profile: Full Name - \(fullName), Email - \(email)")
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
            .padding()
            .navigationTitle("Profile")
        }
    }
    
    struct GroupChatView: View {
        @ObservedObject var group: PeerGroup
        @State private var message = ""
        @State private var username = ""  // Add this line
        
        var body: some View {
            VStack {
                List {
                    ForEach(group.members, id: \.self) { member in
                        Text(member)
                    }
                }
                
                TextField("Type your message", text: $message)
                    .padding()
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                Button("Send Message") {
                    // Implement logic to send messages in the group chat
                    if !message.isEmpty {
                        // For simplicity, add the message to the group members
                        if !username.isEmpty {
                            group.members.append("\(username): \(message)")
                            message = ""
                        } else {
                            // Show an alert for missing username
                            showAlert(title: "Missing Username", message: "Please enter your username.")
                        }
                    }
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
            }
            .padding()
            .navigationTitle(group.name)
            .onAppear {
                // Assign the username when the view appears
                username = UserDefaults.standard.string(forKey: "username") ?? ""
            }
        }
        
        // Helper function to show an alert
        private func showAlert(title: String, message: String) {
            // You can implement an alert here
            print("Alert: \(title) - \(message)")
        }
    }
    
    struct AppointmentView: View {
        @ObservedObject var userData: UserData
        @State private var selectedDate = Date()
        
        var body: some View {
            VStack {
                DatePicker("Select Date", selection: $selectedDate, in: Date()..., displayedComponents: .date)
                    .padding()
                    .datePickerStyle(GraphicalDatePickerStyle())
                
                TextField("Enter Time", text: $userData.appointmentTime)
                    .padding()
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                TextField("Enter Duration (minutes)", text: $userData.appointmentDuration)
                    .padding()
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                
                Button("Schedule Appointment") {
                    let formattedDate = DateFormatter.localizedString(from: selectedDate, dateStyle: .medium, timeStyle: .none)
                    userData.appointments.append(Appointment(date: formattedDate, time: userData.appointmentTime, duration: userData.appointmentDuration))
                    userData.appointmentTime = ""
                    userData.appointmentDuration = ""
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
                
                // Display a list of scheduled appointments
                List {
                    ForEach(userData.appointments) { appointment in
                        VStack(alignment: .leading) {
                            Text("Date: \(appointment.date)")
                            Text("Time: \(appointment.time)")
                            Text("Duration: \(appointment.duration) minutes")
                        }
                        .padding()
                        .background(Color.gray.opacity(0.2))
                        .cornerRadius(8)
                        .padding(.vertical, 5)
                    }
                }
                .padding()
                .navigationTitle("Appointments")
            }
        }
    }
    
    struct SettingsView: View {
        @State private var notificationEnabled = false
        @State private var darkModeEnabled = false
        
        var body: some View {
            Toggle("Enable Notifications", isOn: $notificationEnabled)
                .padding()
            
            Toggle("Dark Mode", isOn: $darkModeEnabled)
                .padding()
            
            Button("Save Settings") {
                // Implement logic to save user settings
                // Use notificationEnabled and darkModeEnabled
            }
            .padding()
            .background(Color.green)
            .foregroundColor(.white)
            .cornerRadius(10)
            
            Text("Settings Updated!")
                .foregroundColor(.green)
                .padding()
        }
    }
    
    struct NotificationsView: View {
        // Sample Notifications View
        var body: some View {
            Text("Notifications View")
                .padding()
                .navigationTitle("Notifications")
        }
    }
    
    struct FeedbackView: View {
        // Sample Feedback View
        var body: some View {
            Text("Feedback View")
                .padding()
                .navigationTitle("Feedback")
        }
    }
    
    struct SecurityView: View {
        // Sample Security View
        var body: some View {
            Text("Security View")
                .padding()
                .navigationTitle("Security")
        }
    }
    
