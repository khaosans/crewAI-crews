import React from 'react'
import Link from 'next/link'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { BarChart, Calendar, CheckCircle, ListTodo, Plus, Settings, Users } from 'lucide-react'

export default function Dashboard() {
    return (
        <div className="p-6 space-y-6">
            <div className="flex justify-between items-center">
                <h1 className="text-3xl font-bold">Dashboard</h1>
                <Button>
                    <Plus className="mr-2 h-4 w-4" /> New Project
                </Button>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
                <Card>
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Total Projects</CardTitle>
                        <ListTodo className="h-4 w-4 text-muted-foreground" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">12</div>
                        <p className="text-xs text-muted-foreground">+2 from last month</p>
                    </CardContent>
                </Card>
                <Card>
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Completed Tasks</CardTitle>
                        <CheckCircle className="h-4 w-4 text-muted-foreground" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">64</div>
                        <p className="text-xs text-muted-foreground">+12% from last week</p>
                    </CardContent>
                </Card>
                <Card>
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Active Team Members</CardTitle>
                        <Users className="h-4 w-4 text-muted-foreground" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">24</div>
                        <p className="text-xs text-muted-foreground">+4 new this month</p>
                    </CardContent>
                </Card>
                <Card>
                    <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <CardTitle className="text-sm font-medium">Upcoming Deadlines</CardTitle>
                        <Calendar className="h-4 w-4 text-muted-foreground" />
                    </CardHeader>
                    <CardContent>
                        <div className="text-2xl font-bold">7</div>
                        <p className="text-xs text-muted-foreground">Within next 7 days</p>
                    </CardContent>
                </Card>
            </div>

            <div className="grid gap-6 md:grid-cols-2">
                <Card>
                    <CardHeader>
                        <CardTitle>Recent Activity</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="space-y-4">
                            {[
                                { user: 'Alice', action: 'completed task', project: 'Website Redesign' },
                                { user: 'Bob', action: 'added new task', project: 'Mobile App' },
                                { user: 'Charlie', action: 'commented on', project: 'Database Migration' },
                                { user: 'Diana', action: 'started project', project: 'AI Integration' },
                            ].map((activity, index) => (
                                <div key={index} className="flex items-center">
                                    <Avatar className="h-9 w-9">
                                        <AvatarImage src={`/avatars/${activity.user.toLowerCase()}.png`} alt={activity.user} />
                                        <AvatarFallback>{activity.user[0]}</AvatarFallback>
                                    </Avatar>
                                    <div className="ml-4 space-y-1">
                                        <p className="text-sm font-medium leading-none">
                                            {activity.user} {activity.action}
                                        </p>
                                        <p className="text-sm text-muted-foreground">
                                            {activity.project}
                                        </p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </CardContent>
                </Card>
                <Card>
                    <CardHeader>
                        <CardTitle>Project Progress</CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="space-y-4">
                            {[
                                { name: 'Website Redesign', progress: 75 },
                                { name: 'Mobile App', progress: 50 },
                                { name: 'Database Migration', progress: 90 },
                                { name: 'AI Integration', progress: 30 },
                            ].map((project, index) => (
                                <div key={index} className="space-y-2">
                                    <div className="flex items-center justify-between">
                                        <p className="text-sm font-medium">{project.name}</p>
                                        <span className="text-sm text-muted-foreground">{project.progress}%</span>
                                    </div>
                                    <Progress value={project.progress} />
                                </div>
                            ))}
                        </div>
                    </CardContent>
                </Card>
            </div>

            <div className="flex justify-between items-center">
                <h2 className="text-2xl font-bold">Your Projects</h2>
                <Button variant="outline">View All</Button>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                {[
                    { name: 'Website Redesign', description: 'Modernizing our company website', progress: 75 },
                    { name: 'Mobile App', description: 'Developing a new mobile application', progress: 50 },
                    { name: 'Database Migration', description: 'Upgrading our database infrastructure', progress: 90 },
                ].map((project, index) => (
                    <Card key={index}>
                        <CardHeader>
                            <CardTitle>{project.name}</CardTitle>
                            <CardDescription>{project.description}</CardDescription>
                        </CardHeader>
                        <CardContent>
                            <div className="flex justify-between items-center mb-2">
                                <span className="text-sm font-medium">Progress</span>
                                <span className="text-sm text-muted-foreground">{project.progress}%</span>
                            </div>
                            <Progress value={project.progress} />
                            <div className="mt-4 flex justify-between">
                                <Button variant="outline" size="sm" asChild>
                                    <Link href={`/project/${project.name.toLowerCase().replace(' ', '-')}`}>
                                        View Board
                                    </Link>
                                </Button>
                                <Button variant="ghost" size="sm" asChild>
                                    <Link href={`/project/${project.name.toLowerCase().replace(' ', '-')}/settings`}>
                                        <Settings className="mr-2 h-4 w-4" />
                                        Settings
                                    </Link>
                                </Button>
                            </div>
                        </CardContent>
                    </Card>
                ))}
            </div>
        </div>
    )
}
