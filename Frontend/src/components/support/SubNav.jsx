import React from "react";
import styled from "styled-components";

import SubNavButton from "components/common/SubNavButton";

const StyledSubNav = styled.nav`
	display: flex;
	justify-content: center;
	margin-bottom: 30px;
`;

const SubNav = (props) => {
	return (
		<StyledSubNav>
			<SubNavButton
				href="/support/sponsorship"
				text="후원하기"
				select={props.select === "후원하기"}
			></SubNavButton>
			<SubNavButton
				href="/support/benefits"
				text="후원자 혜택"
				select={props.select === "후원자 혜택"}
			></SubNavButton>
			<SubNavButton
				href="/support/sponsor"
				text="후원자 소개"
				select={props.select === "후원자 소개"}
			></SubNavButton>
			<SubNavButton
				href="/support/history"
				text="후원금 사용 내역"
				select={props.select === "후원금 사용 내역"}
			></SubNavButton>
		</StyledSubNav>
	);
};

export default SubNav;
