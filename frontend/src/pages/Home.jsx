import { useEffect, useState } from "react";

import Navbar from "../components/Navbar/Navbar";
import Hero from "../components/Hero/Hero";
import SearchBar from "../components/SearchBar/SearchBar";
import EventCard from "../components/EventCard/EventCard";
import SearchSection from "../components/SearchSection/SearchSection";

import api from "../services/api";

function Home() {

    const [events, setEvents] = useState([]);
    const [search, setSearch] = useState("");

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
    const filteredEvents = events.filter((event)=>{

    const text = (
        event.title +
        event.city +
        event.state +
        event.category
    ).toLowerCase();

    return text.includes(search.toLowerCase());

    });
    return (

        <>

            <Navbar />

            <Hero />

            <SearchSection

            total={filteredEvents.length}

            search={search}

            setSearch={setSearch}

            />


            <section className="cards">

                {

                    filteredEvents.map((event) => (
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