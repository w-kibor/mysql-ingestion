import { NextResponse } from 'next/server';
import mysql from 'mysql2/promise';

export async function GET() {
    try {
        const connection = await mysql.createConnection({
            host: process.env.DB_HOST,
            user: process.env.DB_USER,
            password: process.env.DB_PASSWORD,
            database: process.env.DB_NAME,
            port: Number(process.env.DB_PORT),
        });

        const [rows] = await connection.execute(
            'SELECT * FROM articles ORDER BY posted_at DESC LIMIT 50'
        );

        await connection.end();

        return NextResponse.json(rows);
    } catch (error) {
        console.error('Database connection error:', error);
        return NextResponse.json(
            { error: 'Failed to fetch news' },
            { status: 500 }
        );
    }
}
