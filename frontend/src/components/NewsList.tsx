'use client';

import { useState, useEffect } from 'react';

interface Article {
    id: number;
    title: string;
    url: string;
    author: string;
    score: number;
    posted_at: string;
    category: string;
}

export default function NewsList() {
    const [articles, setArticles] = useState<Article[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        async function fetchNews() {
            try {
                const res = await fetch('/api/news');
                if (!res.ok) {
                    throw new Error('Failed to fetch news');
                }
                const data = await res.json();
                setArticles(data);
            } catch (err) {
                setError(err instanceof Error ? err.message : 'An error occurred');
            } finally {
                setLoading(false);
            }
        }

        fetchNews();
    }, []);

    if (loading) {
        return (
            <div className="flex justify-center items-center py-20">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-pink-500"></div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="text-center py-10 text-red-500">
                Error: {error}
            </div>
        );
    }

    return (
        <div className="space-y-4">
            {articles.map((article) => (
                <a
                    key={article.id}
                    href={article.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="block p-6 bg-white border border-pink-100 rounded-lg shadow-sm hover:bg-pink-50 hover:shadow-md transition-all duration-200"
                >
                    <div className="flex justify-between items-start gap-4">
                        <h2 className="text-xl font-semibold text-gray-900 leading-tight group-hover:text-pink-600">
                            {article.title}
                        </h2>
                        <span className="shrink-0 bg-pink-100 text-pink-800 text-xs font-medium px-2.5 py-0.5 rounded-full">
                            {article.score} pts
                        </span>
                    </div>

                    <div className="mt-3 flex items-center gap-4 text-sm text-gray-600">
                        <div className="flex items-center gap-1">
                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                            </svg>
                            {article.author}
                        </div>

                        <div className="flex items-center gap-1">
                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            {new Date(article.posted_at).toLocaleDateString()}
                        </div>

                        <span className="text-gray-400">•</span>
                        <span>{new URL(article.url || 'https://news.ycombinator.com').hostname.replace('www.', '')}</span>
                    </div>
                </a>
            ))}
        </div>
    );
}
