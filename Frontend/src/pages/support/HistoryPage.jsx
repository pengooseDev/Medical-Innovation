import React from "react";

import BoardPage from "../BoardPage";
import SubNav from "../../components/support/SubNav";

const HistoryPage = () => {
	return (
		<BoardPage boardId="1">
			<SubNav select="후원금 사용 내역" />
			<h1>재정 보고</h1>
		</BoardPage>
	);
};

export default HistoryPage;
