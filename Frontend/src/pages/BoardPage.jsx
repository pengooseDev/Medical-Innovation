import React, { useState, useEffect } from "react";
import styled from "styled-components";

import Page from "../components/common/Page";

const BoardPage = ({ boardId, children }) => {
	const SIZE = 20;
	const [total, setTotal] = useState(0);
	const [page, setPage] = useState(0);
	const [posts, setPosts] = useState([]);

	useEffect(() => {
		fetch(
			`http://127.0.0.1:8000/api/v1/post/${boardId}/all?limit=${SIZE}&skip=${page}`,
			{
				method: "GET",
				headers: {
					accept: "application/json",
				},
			}
		).then((res) => {
			if (res.status === 200) {
				res.json().then((data) => {
					setPosts(data.posts);
					setTotal(data.total);
					console.log(data);
				});
			}
		});
	}, [page, boardId]);

	return (
		<Page>
			{children}
			<div>
				{posts.map((item, index) => {
					return <PostItem idx={index} item={item} page={page} />;
				})}
			</div>
			<StyledBoardPageButtonWrapper>
				<StyledBoardPageButton
					onClick={() => setPage(Math.max(0, page - SIZE))}
					disabled={page <= 0}
				>
					이전
				</StyledBoardPageButton>
				{Array.from({ length: Math.ceil(total / SIZE) }).map((_, index) => {
					return (
						<StyledBoardPageButton
							onClick={() => setPage(index * SIZE)}
							disabled={index * SIZE === page}
						>
							{index * SIZE}
						</StyledBoardPageButton>
					);
				})}

				<StyledBoardPageButton
					onClick={() => setPage(Math.min(total, page + SIZE))}
					disabled={page >= total / SIZE - 1}
				>
					다음
				</StyledBoardPageButton>
			</StyledBoardPageButtonWrapper>
		</Page>
	);
};

const StyledPostItem = styled.div`
	display: flex;
	align-items: center;
	padding: 15px 0;

	&:hover {
		background-color: #f9f9f9;
	}
	&:hover a {
		text-decoration: underline;
	}

	& + & {
		border-top: 1px solid #ececec;
	}

	& > span {
		width: 10%;
		text-align: center;
		font-size: 16px;
		font-weight: 400;
		line-height: 22px;
	}

	& > div > span {
		font-size: 12px;
		display: block;
	}

	& a {
		color: #000000;
	}
`;

const StyledPostItemContent = styled.div`
	width: 73%;
	margin-right: 1%;
	display: flex;
	flex-direction: column;

	& > a {
		font-size: 16px;
		display: block;
	}
`;

const StyledPostItemButton = styled.div`
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	border: 1px solid #ececec;
	width: 10%;
	padding: 5px;

	& a {
		font-size: 12px;
	}
`;

const PostItem = ({ idx, item, page }) => {
	const date = new Intl.DateTimeFormat("ko", {
		dateStyle: "long",
	}).format(new Date(item.created_at));

	return (
		<StyledPostItem>
			<span>{page + idx + 1}</span>
			<StyledPostItemContent>
				<a href={`/post/${item.id}`}>{item.title}</a>
				<span>게시일 {date}</span>
			</StyledPostItemContent>
			{item.files.length > 0 ? (
				<StyledPostItemButton>
					<a
						href={`http://127.0.0.1:8000/api/v1/file/download/${item.files[0]}`}
						target="_blank"
						rel="noopener noreferrer"
					>
						다운로드
					</a>
				</StyledPostItemButton>
			) : null}
		</StyledPostItem>
	);
};

const StyledBoardPageButtonWrapper = styled.div`
	display: flex;
	justify-content: center;
	align-items: center;
`;

const StyledBoardPageButton = styled.button`
	background-color: #ffffff;
	padding: 6px;
	width: 50px;
	height: 30px;

	& + & {
		margin-left: 5px;
	}
`;

export default BoardPage;
