; ModuleID = 'algorithms/02_c/data_structures/segment_tree.c'
source_filename = "algorithms/02_c/data_structures/segment_tree.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@tree = internal unnamed_addr global [400000 x i64] zeroinitializer, align 16
@str = private unnamed_addr constant [50 x i8] c"[C SegmentTree] Point update + range sum verified\00", align 1
@str.3 = private unnamed_addr constant [42 x i8] c"[C SegmentTree] FAILED: post-update query\00", align 1
@str.4 = private unnamed_addr constant [38 x i8] c"[C SegmentTree] FAILED: initial query\00", align 1

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local void @seg_build(ptr noundef %0, i32 noundef %1, i32 noundef %2, i32 noundef %3) local_unnamed_addr #0 {
  %5 = icmp eq i32 %2, %3
  br i1 %5, label %6, label %14

6:                                                ; preds = %4
  %7 = sext i32 %2 to i64
  %8 = getelementptr inbounds i64, ptr %0, i64 %7
  %9 = load i64, ptr %8, align 8, !tbaa !9
  br label %10

10:                                               ; preds = %6, %14
  %11 = phi i64 [ %9, %6 ], [ %26, %14 ]
  %12 = sext i32 %1 to i64
  %13 = getelementptr inbounds i64, ptr @tree, i64 %12
  store i64 %11, ptr %13, align 8, !tbaa !9
  ret void

14:                                               ; preds = %4
  %15 = add nsw i32 %3, %2
  %16 = sdiv i32 %15, 2
  %17 = shl nsw i32 %1, 1
  tail call void @seg_build(ptr noundef %0, i32 noundef %17, i32 noundef %2, i32 noundef %16)
  %18 = or disjoint i32 %17, 1
  %19 = add nsw i32 %16, 1
  tail call void @seg_build(ptr noundef %0, i32 noundef %18, i32 noundef %19, i32 noundef %3)
  %20 = sext i32 %17 to i64
  %21 = getelementptr inbounds i64, ptr @tree, i64 %20
  %22 = load i64, ptr %21, align 16, !tbaa !9
  %23 = sext i32 %18 to i64
  %24 = getelementptr inbounds i64, ptr @tree, i64 %23
  %25 = load i64, ptr %24, align 8, !tbaa !9
  %26 = add nsw i64 %25, %22
  br label %10
}

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.start.p0(ptr captures(none)) #1

; Function Attrs: mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite)
declare void @llvm.lifetime.end.p0(ptr captures(none)) #1

; Function Attrs: nofree nosync nounwind sspstrong memory(readwrite, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local void @seg_update(i32 noundef %0, i32 noundef %1, i32 noundef %2, i32 noundef %3, i64 noundef %4) local_unnamed_addr #2 {
  %6 = icmp eq i32 %1, %2
  br i1 %6, label %23, label %7

7:                                                ; preds = %5
  %8 = add nsw i32 %2, %1
  %9 = sdiv i32 %8, 2
  %10 = icmp sgt i32 %3, %9
  %11 = shl nsw i32 %0, 1
  br i1 %10, label %13, label %12

12:                                               ; preds = %7
  tail call void @seg_update(i32 noundef %11, i32 noundef %1, i32 noundef %9, i32 noundef %3, i64 noundef %4)
  br label %16

13:                                               ; preds = %7
  %14 = or disjoint i32 %11, 1
  %15 = add nsw i32 %9, 1
  tail call void @seg_update(i32 noundef %14, i32 noundef %15, i32 noundef %2, i32 noundef %3, i64 noundef %4)
  br label %16

16:                                               ; preds = %13, %12
  %17 = sext i32 %11 to i64
  %18 = getelementptr inbounds i64, ptr @tree, i64 %17
  %19 = load i64, ptr %18, align 16, !tbaa !9
  %20 = getelementptr i8, ptr %18, i64 8
  %21 = load i64, ptr %20, align 8, !tbaa !9
  %22 = add nsw i64 %21, %19
  br label %23

23:                                               ; preds = %5, %16
  %24 = phi i64 [ %22, %16 ], [ %4, %5 ]
  %25 = sext i32 %0 to i64
  %26 = getelementptr inbounds i64, ptr @tree, i64 %25
  store i64 %24, ptr %26, align 8, !tbaa !9
  ret void
}

; Function Attrs: nofree nosync nounwind sspstrong memory(read, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local i64 @seg_query(i32 noundef %0, i32 noundef %1, i32 noundef %2, i32 noundef %3, i32 noundef %4) local_unnamed_addr #3 {
  %6 = icmp sgt i32 %3, %2
  %7 = icmp slt i32 %4, %1
  %8 = or i1 %6, %7
  br i1 %8, label %30, label %9

9:                                                ; preds = %5
  %10 = icmp sgt i32 %2, %4
  br label %11

11:                                               ; preds = %9, %21
  %12 = phi i32 [ %1, %9 ], [ %27, %21 ]
  %13 = phi i32 [ %0, %9 ], [ %26, %21 ]
  %14 = phi i64 [ 0, %9 ], [ %28, %21 ]
  %15 = icmp sgt i32 %3, %12
  %16 = or i1 %10, %15
  br i1 %16, label %21, label %17

17:                                               ; preds = %11
  %18 = sext i32 %13 to i64
  %19 = getelementptr inbounds i64, ptr @tree, i64 %18
  %20 = load i64, ptr %19, align 8, !tbaa !9
  br label %30

21:                                               ; preds = %11
  %22 = add nsw i32 %12, %2
  %23 = sdiv i32 %22, 2
  %24 = shl nsw i32 %13, 1
  %25 = tail call i64 @seg_query(i32 noundef %24, i32 noundef %12, i32 noundef %23, i32 noundef %3, i32 noundef %4)
  %26 = or disjoint i32 %24, 1
  %27 = add nsw i32 %23, 1
  %28 = add nsw i64 %25, %14
  %29 = icmp sgt i32 %4, %23
  br i1 %29, label %11, label %30

30:                                               ; preds = %21, %5, %17
  %31 = phi i64 [ %14, %17 ], [ 0, %5 ], [ %28, %21 ]
  %32 = phi i64 [ %20, %17 ], [ 0, %5 ], [ 0, %21 ]
  %33 = add nsw i64 %32, %31
  ret i64 %33
}

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #4 {
  %1 = alloca [5 x i64], align 16
  call void @llvm.lifetime.start.p0(ptr nonnull %1) #6
  store i64 1, ptr %1, align 16
  %2 = getelementptr inbounds nuw i8, ptr %1, i64 8
  store i64 2, ptr %2, align 8
  %3 = getelementptr inbounds nuw i8, ptr %1, i64 16
  store i64 3, ptr %3, align 16
  %4 = getelementptr inbounds nuw i8, ptr %1, i64 24
  store i64 4, ptr %4, align 8
  %5 = getelementptr inbounds nuw i8, ptr %1, i64 32
  store i64 5, ptr %5, align 16
  call void @seg_build(ptr noundef nonnull %1, i32 noundef 1, i32 noundef 0, i32 noundef 4)
  %6 = call i64 @seg_query(i32 noundef 1, i32 noundef 0, i32 noundef 4, i32 noundef 0, i32 noundef 4)
  %7 = icmp eq i64 %6, 15
  br i1 %7, label %8, label %19

8:                                                ; preds = %0
  %9 = call i64 @seg_query(i32 noundef 1, i32 noundef 0, i32 noundef 4, i32 noundef 1, i32 noundef 3)
  %10 = icmp eq i64 %9, 9
  br i1 %10, label %11, label %19

11:                                               ; preds = %8
  call void @seg_update(i32 noundef 1, i32 noundef 0, i32 noundef 4, i32 noundef 2, i64 noundef 10)
  %12 = call i64 @seg_query(i32 noundef 1, i32 noundef 0, i32 noundef 4, i32 noundef 0, i32 noundef 4)
  %13 = icmp eq i64 %12, 22
  br i1 %13, label %14, label %19

14:                                               ; preds = %11
  %15 = call i64 @seg_query(i32 noundef 1, i32 noundef 0, i32 noundef 4, i32 noundef 2, i32 noundef 2)
  %16 = icmp ne i64 %15, 10
  %17 = select i1 %16, ptr @str.3, ptr @str
  %18 = zext i1 %16 to i32
  br label %19

19:                                               ; preds = %14, %11, %0, %8
  %20 = phi ptr [ @str.3, %11 ], [ @str.4, %0 ], [ @str.4, %8 ], [ %17, %14 ]
  %21 = phi i32 [ 1, %11 ], [ 1, %0 ], [ 1, %8 ], [ %18, %14 ]
  %22 = call i32 @puts(ptr nonnull dereferenceable(1) %20)
  call void @llvm.lifetime.end.p0(ptr nonnull %1) #6
  ret i32 %21
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #5

attributes #0 = { nofree nosync nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nosync nounwind willreturn memory(argmem: readwrite) }
attributes #2 = { nofree nosync nounwind sspstrong memory(readwrite, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nosync nounwind sspstrong memory(read, argmem: none, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #4 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #5 = { nofree nounwind }
attributes #6 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!10, !10, i64 0}
!10 = !{!"long long", !7, i64 0}
