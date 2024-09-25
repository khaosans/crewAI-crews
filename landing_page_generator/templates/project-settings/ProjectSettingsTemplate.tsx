
import React from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Badge } from "@/components/ui/badge"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Switch } from "@/components/ui/switch"

export default function ProjectSettings() {
    return (
        <div className="container mx-auto p-6 space-y-8">
            <div className="flex justify-between items-center">
                <h1 className="text-3xl font-bold">Project Settings</h1>
                <Button>Save Changes</Button>
            </div>

            <div className="grid gap-6 md:grid-cols-2">
                <Card>
                    <CardHeader>
                        <CardTitle>General Information</CardTitle>
                        <CardDescription>Basic details about your project.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <div className="space-y-2">
                            <Label htmlFor="projectName">Project Name</Label>
                            <Input id="projectName" defaultValue="Website Redesign" />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="projectDescription">Description</Label>
                            <Textarea id="projectDescription" defaultValue="A complete overhaul of our company website to improve user experience and modernize our online presence." />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="projectStatus">Project Status</Label>
                            <Select defaultValue="in-progress">
                                <SelectTrigger>
                                    <SelectValue placeholder="Select status" />
                                </SelectTrigger>
                                <SelectContent>
                                    <SelectItem value="planning">Planning</SelectItem>
                                    <SelectItem value="in-progress">In Progress</SelectItem>
                                    <SelectItem value="on-hold">On Hold</SelectItem>
                                    <SelectItem value="completed">Completed</SelectItem>
                                </SelectContent>
                            </Select>
                        </div>
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>Team Members</CardTitle>
                        <CardDescription>Manage who has access to this project.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        {[
                            { name: 'Alice Johnson', role: 'Project Manager', avatar: '/avatars/alice.png' },
                            { name: 'Bob Smith', role: 'Developer', avatar: '/avatars/bob.png' },
                            { name: 'Charlie Davis', role: 'Designer', avatar: '/avatars/charlie.png' },
                        ].map((member, index) => (
                            <div key={index} className="flex items-center justify-between">
                                <div className="flex items-center space-x-4">
                                    <Avatar>
                                        <AvatarImage src={member.avatar} alt={member.name} />
                                        <AvatarFallback>{member.name[0]}</AvatarFallback>
                                    </Avatar>
                                    <div>
                                        <p className="font-medium">{member.name}</p>
                                        <p className="text-sm text-muted-foreground">{member.role}</p>
                                    </div>
                                </div>
                                <Button variant="outline" size="sm">Remove</Button>
                            </div>
                        ))}
                        <Button className="w-full">Add Team Member</Button>
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>Project Timeline</CardTitle>
                        <CardDescription>Set the start and end dates for your project.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <div className="space-y-2">
                            <Label htmlFor="startDate">Start Date</Label>
                            <Input id="startDate" type="date" defaultValue="2023-01-01" />
                        </div>
                        <div className="space-y-2">
                            <Label htmlFor="endDate">End Date</Label>
                            <Input id="endDate" type="date" defaultValue="2023-12-31" />
                        </div>
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>Tags</CardTitle>
                        <CardDescription>Categorize your project for easy filtering.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <div className="flex flex-wrap gap-2">
                            {['Web Development', 'Design', 'Marketing', 'High Priority'].map((tag, index) => (
                                <Badge key={index} variant="secondary">{tag}</Badge>
                            ))}
                        </div>
                        <div className="flex space-x-2">
                            <Input placeholder="Add new tag" />
                            <Button>Add</Button>
                        </div>
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>Notifications</CardTitle>
                        <CardDescription>Configure how you receive updates about this project.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        {[
                            { label: 'Email Notifications', description: 'Receive project updates via email' },
                            { label: 'Push Notifications', description: 'Get notified on your device' },
                            { label: 'Daily Digest', description: 'Receive a summary of activities each day' },
                        ].map((item, index) => (
                            <div key={index} className="flex items-center justify-between">
                                <div>
                                    <p className="font-medium">{item.label}</p>
                                    <p className="text-sm text-muted-foreground">{item.description}</p>
                                </div>
                                <Switch />
                            </div>
                        ))}
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>Danger Zone</CardTitle>
                        <CardDescription>Irreversible actions for your project.</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <div className="space-y-2">
                            <h3 className="font-medium">Archive Project</h3>
                            <p className="text-sm text-muted-foreground">This will archive the project and make it read-only.</p>
                            <Button variant="outline">Archive Project</Button>
                        </div>
                        <div className="space-y-2">
                            <h3 className="font-medium">Delete Project</h3>
                            <p className="text-sm text-muted-foreground">This action cannot be undone. All project data will be permanently removed.</p>
                            <Button variant="destructive">Delete Project</Button>
                        </div>
                    </CardContent>
                </Card>
            </div>
        </div>
    )
}
