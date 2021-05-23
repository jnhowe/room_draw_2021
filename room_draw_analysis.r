library(readr)
library(dplyr)
history = read_csv("2019_room_draw_times.csv")
butler = read_csv("2021_butler_draw.csv")
mathey = read_csv("2021_mathey_draw.csv")
spelman = read_csv("2021_spellman_draw.csv")
independent = read_csv("2021_independent_draw.csv")
upperclassman = read_csv("2021_upperclassmen_draw.csv")
whitman = read_csv("2021_whitman_draw.csv")
all_rooms = read_csv("all_available_rooms.csv")

# order of room draw
# butler 5/27/20219:00
# independent 5/25/20219:00
# Mathey 5/27/20219:00
# spelman 5/24/20219:00
# upperclass 6/9/20218:00
# whitman 5/27/20219:00

# spellman > independent > butler = mathey = whitman = forbes? > upperclass

# add indices so that we know the order of people.
butler$index = c(1:nrow(butler))
mathey$index = c(1:nrow(mathey))
independent$index = c(1:nrow(independent))
spelman$index = c(1:nrow(spelman))
upperclassman$index = c(1:nrow(upperclassman))
whitman$index = c(1:nrow(whitman))
history$index = c(1:nrow(history))


history$Building = toupper(history$Building)

missing = anti_join( all_rooms, history,by = c("Building" = "Building", "Room"="Room"))

info = left_join(all_rooms,history, by = c("Building" = "Building", "Room"="Room"))

# last name then first name
name = "Howe Jafar"

where_am_i = function(name){
    print("Butler")
    butler %>% filter(Name == name) %>%  print()
    print("Mathey")
    mathey %>% filter(Name == name) %>%  print()
    print("Independent")
    independent %>% filter(Name == name)%>%  print()
    print("Whitman")
    whitman %>% filter(Name == name)%>%  print()
    print("Upperclassman")
    upperclassman %>% filter(Name == name)%>%  print()
    print("Spelman")
    spelman %>% filter(Name == name)%>%  print()
}
where_am_i(name)

# My times:
# Spelman = 5/24/2021 16:36
# Independent = 5/26/2021 15:12
# Butler = 5/28/2021 11:18
# Mathey = 5/28/2021 16:40
# Upperclassman = 6/23/2021 10:34

before_me = butler %>% filter(index < 343)
anti_join(before_me, spelman, by = c("Name" = "Name")) %>% nrow()

info %>% filter(Building == "SCULLY") %>% arrange(index) %>% View()

