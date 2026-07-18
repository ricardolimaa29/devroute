import { useEffect, useState } from "react";

import Navbar from "../components/Navbar/Navbar";
import Hero from "../components/Hero/Hero";
import SearchBar from "../components/SearchBar/SearchBar";
import EventCard from "../components/EventCard/EventCard";

import api from "../services/api";

function Home() {

    const [events, setEvents] = useState([]);

    useEffect(() => {

        loadEvents();

    }, []);

    async function loadEvents() {

        try {

            const response = await api.get("/events");

            console.log(response.data);

            setEvents(response.data);
            console.log(response.data);

            setEvents(response.data);

            console.log(response.data.length);


        } catch (error) {

            console.error(error);

        }

    }
    console.log(events);
    return (

        <>

            <Navbar />

            <Hero />

            <SearchBar />

            <section className="cards">

                {

                    events.map((event) => (
                            <EventCard

                                key={event.id}

                                titulo={event.title}

                                cidade={event.city}

                                estado={event.state}

                                data={event.start_date}

                                categoria={event.category}

                                modalidade={event.modality}

                                url={event.url}

                            />

                    ))

                }

            </section>

        </>

    );

}

export default Home;