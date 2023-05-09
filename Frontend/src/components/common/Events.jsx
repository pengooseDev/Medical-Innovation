import React from "react";
import styled from "styled-components";

import { API_URL, CDN_URL } from "utils/const";
import { Link } from "react-router-dom";

const StyledEvents = styled.div`
	display: grid;
	grid-template-columns: repeat(3, 1fr);
	column-gap: 15px;
	grid-gap: 30px;

	@media screen and (max-width: 991px) {
		grid-template-columns: repeat(2, 1fr);
		grid-gap: 8px;
	}
	@media screen and (min-width: 450px) and (max-width: 991px) {
		grid-template-columns: repeat(2, 1fr);
		grid-gap: 10px;
	}
	@media screen and (min-width: 992px) and (max-width: 1249px) {
		grid-template-columns: repeat(2, 1fr);
		grid-gap: 30px;
	}
	@media screen and (min-width: 1250px) {
	}
`;

const Events = ({ events, itemToLink }) => {
	return (
		<StyledEvents>
			{events.map((item) => {
				return <EventItem item={item} itemToLink={itemToLink} />;
			})}
		</StyledEvents>
	);
};

const StyledEventItem = styled.div`
	border: 1px solid #eaeaea;
	border-radius: 10px;

	padding: 15px;

	width: 300px;
	height: 400px;
	overflow: hidden;

	& div {
		height: 200px;
		overflow: hidden;
		border: 1px solid #eaeaea;
		border-radius: 10px;
	}

	& img {
		object-fit: cover;
		width: 100%;
		height: 100%;
	}

	& h2 {
		font-size: 20px;
		word-break: keep-all;
	}

	& span {
		font-size: 16px;
		color: rgb(80, 80, 80);
	}

	& a {
		color: #0000ff;
	}

	@media screen and (max-width: 991px) {
		height: 300px;

		& div {
			height: 150px;
			overflow: hidden;
			border: 1px solid #eaeaea;
			border-radius: 10px;
		}

		& img {
			object-fit: cover;
			width: 100%;
			height: 100%;
		}

		& h2 {
			font-size: 16px;
			word-break: keep-all;
		}
	}

	@media screen and (max-width: 450px) {
		width: 150px;
	}
`;

const EventItem = ({ item, itemToLink }) => {
	return (
		<StyledEventItem>
			<div>
				<img
					src={`${CDN_URL}/upload/${
						item.thumbnail_filename ? item.thumbnail_filename : "null.png"
					}`}
					alt={item.name}
				/>
			</div>
			<br />
			<span>{item.start_date || item.join_start_date}</span>
			<h2>{item.name}</h2>
			<Link to={itemToLink(item)}>자세히 보기</Link>
		</StyledEventItem>
	);
};

export default Events;
